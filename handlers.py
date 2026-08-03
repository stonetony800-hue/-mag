"""
=========================================================
AlgoPipX Educational Assistant
User Handlers
=========================================================
"""

from telegram import Update
from telegram.ext import (
    ContextTypes
)

from database import (
    add_user,
    update_language,
    get_user_language
)

from languages import get_text

from keyboards import (
    main_menu_keyboard,
    back_button,
    faq_keyboard,
    language_keyboard,
    guides_keyboard
)

from faq import (
    load_faqs,
    fetch_faq,
    format_faq
)



# -------------------------------------------------------
# START COMMAND
# -------------------------------------------------------

async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user


    add_user(
        user.id,
        user.username,
        user.first_name
    )


    language = get_user_language(
        user.id
    )


    await update.message.reply_text(

        get_text(
            language,
            "welcome"
        ),

        reply_markup=main_menu_keyboard()

    )



# -------------------------------------------------------
# BUTTON CALLBACK HANDLER
# -------------------------------------------------------

async def button_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()


    user_id = query.from_user.id


    language = get_user_language(
        user_id
    )


    data = query.data



    # ---------------------------
    # Main Menu
    # ---------------------------

    if data == "main_menu":

        await query.message.edit_text(

            get_text(
                language,
                "welcome"
            ),

            reply_markup=main_menu_keyboard()

        )



    # ---------------------------
    # Guides
    # ---------------------------

    elif data == "guides":

        await query.message.edit_text(

            get_text(
                language,
                "guides"
            ),

            reply_markup=guides_keyboard()

        )



    elif data == "market_analysis":

        await query.message.edit_text(

            get_text(
                language,
                "market_analysis"
            ),

            reply_markup=back_button()

        )



    elif data == "automation":

        await query.message.edit_text(

            get_text(
                language,
                "automation"
            ),

            reply_markup=back_button()

        )



    elif data == "risk_management":

        await query.message.edit_text(

            get_text(
                language,
                "risk_management"
            ),

            reply_markup=back_button()

        )



    elif data == "strategy":

        await query.message.edit_text(

            get_text(
                language,
                "strategy"
            ),

            reply_markup=back_button()

        )



    # ---------------------------
    # About
    # ---------------------------

    elif data == "about":

        await query.message.edit_text(

            get_text(
                language,
                "about"
            ),

            reply_markup=back_button()

        )



    # ---------------------------
    # FAQ Menu
    # ---------------------------

    elif data == "faq_menu":

        faqs = load_faqs()


        if not faqs:

            await query.message.edit_text(

                get_text(
                    language,
                    "faq_empty"
                ),

                reply_markup=back_button()

            )

            return



        await query.message.edit_text(

            "❓ Frequently Asked Questions",

            reply_markup=faq_keyboard(faqs)

        )



    # ---------------------------
    # FAQ Answer
    # ---------------------------

    elif data.startswith(
        "faq_"
    ):

        faq_id = data.split(
            "_"
        )[1]


        faq = fetch_faq(
            faq_id
        )


        if faq:

            await query.message.edit_text(

                format_faq(
                    faq[0],
                    faq[1]
                ),

                reply_markup=back_button()

            )



    # ---------------------------
    # Language Menu
    # ---------------------------

    elif data == "language_menu":

        await query.message.edit_text(

            "🌍 Select Language",

            reply_markup=language_keyboard()

        )



    # ---------------------------
    # Language Change
    # ---------------------------

    elif data.startswith(
        "lang_"
    ):

        lang = data.split(
            "_"
        )[1]


        update_language(
            user_id,
            lang
        )


        await query.message.edit_text(

            get_text(
                lang,
                "language_changed"
            ),

            reply_markup=main_menu_keyboard()

        )
