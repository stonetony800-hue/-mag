"""
=========================================================
AlgoPipX Educational Assistant
Webhook Server
=========================================================
"""

import logging

from aiohttp import web

from telegram import Update

from telegram.ext import Application


from config import (
    BOT_TOKEN,
    WEBHOOK_URL,
    PORT
)


from database import init_database

from faq import setup_default_faqs



# -------------------------------------------------------
# Logging
# -------------------------------------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)



# -------------------------------------------------------
# Telegram Webhook Handler
# -------------------------------------------------------

async def telegram_webhook(request):

    bot_app = request.app["bot_app"]


    data = await request.json()


    update = Update.de_json(
        data,
        bot_app.bot
    )


    await bot_app.process_update(
        update
    )


    return web.Response(
        status=200
    )



# -------------------------------------------------------
# Health Check
# -------------------------------------------------------

async def health_check(request):

    return web.Response(

        text="AlgoPipX Bot is running",

        status=200

    )



# -------------------------------------------------------
# Startup
# -------------------------------------------------------

async def startup(app):

    if not BOT_TOKEN:

        raise ValueError(
            "Missing TELEGRAM_TOKEN"
        )


    if not WEBHOOK_URL:

        raise ValueError(
            "Missing WEBHOOK_URL"
        )


    # Database setup

    init_database()


    # Default FAQ setup

    setup_default_faqs()



    bot_app = Application.builder().token(
        BOT_TOKEN
    ).build()



    from handlers import (
        start,
        button_handler
    )


    from admin import (
        admin_panel,
        statistics,
        broadcast,
        add_faq_command,
        delete_faq_command
    )



    # ---------------------------
    # User Commands
    # ---------------------------

    from telegram.ext import (
        CommandHandler,
        CallbackQueryHandler
    )


    bot_app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )



    # ---------------------------
    # Admin Commands
    # ---------------------------

    bot_app.add_handler(

        CommandHandler(
            "admin",
            admin_panel
        )

    )


    bot_app.add_handler(

        CommandHandler(
            "stats",
            statistics
        )

    )


    bot_app.add_handler(

        CommandHandler(
            "broadcast",
            broadcast
        )

    )


    bot_app.add_handler(

        CommandHandler(
            "addfaq",
            add_faq_command
        )

    )


    bot_app.add_handler(

        CommandHandler(
            "deletefaq",
            delete_faq_command
        )

    )



    # Buttons

    bot_app.add_handler(

        CallbackQueryHandler(
            button_handler
        )

    )



    await bot_app.initialize()

    await bot_app.start()



    await bot_app.bot.set_webhook(

        url=f"{WEBHOOK_URL}/webhook"

    )


    app["bot_app"] = bot_app


    logger.info(
        "Telegram webhook successfully connected"
    )



# -------------------------------------------------------
# Shutdown
# -------------------------------------------------------

async def shutdown(app):

    bot_app = app.get(
        "bot_app"
    )


    if bot_app:

        await bot_app.stop()

        await bot_app.shutdown()



# -------------------------------------------------------
# Create Web App
# -------------------------------------------------------

def create_app():

    app = web.Application()


    app.router.add_post(
        "/webhook",
        telegram_webhook
    )


    app.router.add_get(
        "/",
        health_check
    )


    app.router.add_get(
        "/health",
        health_check
    )


    app.on_startup.append(
        startup
    )


    app.on_cleanup.append(
        shutdown
    )


    return app
