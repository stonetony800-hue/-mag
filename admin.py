"""
=========================================================
AlgoPipX Educational Assistant
Admin Manager
=========================================================
"""

from telegram import Update
from telegram.ext import (
    ContextTypes
)

from config import ADMIN_IDS

from database import (
    get_user_count,
    get_all_users
)

from faq import (
    create_faq,
    remove_faq
)

from keyboards import admin_keyboard


# -------------------------------------------------------
# Admin Check
# -------------------------------------------------------

def is_admin(user_id):

    return user_id in ADMIN_IDS



# -------------------------------------------------------
# Admin Panel
# -------------------------------------------------------

async def admin_panel(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if not is_admin(user_id):

        await update.message.reply_text(
            "❌ You are not authorized."
        )

        return


    await update.message.reply_text(
        "⚙️ Admin Panel",
        reply_markup=admin_keyboard()
    )



# -------------------------------------------------------
# Statistics
# -------------------------------------------------------

async def statistics(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if not is_admin(user_id):
        return


    total = get_user_count()


    await update.message.reply_text(

        f"📊 Bot Statistics\n\n"
        f"👥 Total Users: {total}"

    )



# -------------------------------------------------------
# Broadcast
# -------------------------------------------------------

async def broadcast(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if not is_admin(user_id):

        return


    if not context.args:

        await update.message.reply_text(

            "Usage:\n"
            "/broadcast Your message"

        )

        return



    message = " ".join(
        context.args
    )


    users = get_all_users()


    sent = 0


    for user in users:

        try:

            await context.bot.send_message(

                chat_id=user,

                text=message

            )

            sent += 1


        except Exception:

            continue



    await update.message.reply_text(

        f"✅ Broadcast completed\n\n"
        f"Sent: {sent}/{len(users)}"

    )



# -------------------------------------------------------
# Add FAQ
# -------------------------------------------------------

async def add_faq_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if not is_admin(user_id):

        return



    if len(context.args) < 2:

        await update.message.reply_text(

            "Usage:\n"
            "/addfaq Question | Answer"

        )

        return



    text = " ".join(
        context.args
    )


    if "|" not in text:

        await update.message.reply_text(

            "Separate question and answer using |"

        )

        return



    question, answer = text.split(
        "|",
        1
    )


    create_faq(
        question,
        answer
    )


    await update.message.reply_text(

        "✅ FAQ added successfully."

    )



# -------------------------------------------------------
# Delete FAQ
# -------------------------------------------------------

async def delete_faq_command(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user_id = update.effective_user.id


    if not is_admin(user_id):

        return



    if not context.args:

        await update.message.reply_text(

            "Usage:\n"
            "/deletefaq FAQ_ID"

        )

        return



    result = remove_faq(
        context.args[0]
    )


    if result:

        await update.message.reply_text(

            "✅ FAQ deleted."

        )

    else:

        await update.message.reply_text(

            "❌ Unable to delete FAQ."

        )
