"""
=========================================================
AlgoPipX Educational Assistant
Keyboard Manager
=========================================================
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    CHANNEL_LINK,
    SUPPORT_USERNAME,
    SUPPORTED_LANGUAGES
)


# -------------------------------------------------------
# Main Menu
# -------------------------------------------------------

def main_menu_keyboard():

    keyboard = [

        [
            InlineKeyboardButton(
                "📚 Educational Guides",
                callback_data="guides"
            )
        ],

        [
            InlineKeyboardButton(
                "❓ FAQ",
                callback_data="faq_menu"
            )
        ],

        [
            InlineKeyboardButton(
                "📢 Join Channel",
                url=CHANNEL_LINK
            )
        ],

        [
            InlineKeyboardButton(
                "☎️ Contact Support",
                url=f"https://t.me/{SUPPORT_USERNAME.replace('@','')}"
            )
        ],

        [
            InlineKeyboardButton(
                "🌍 Language",
                callback_data="language_menu"
            )
        ],

        [
            InlineKeyboardButton(
                "ℹ️ About",
                callback_data="about"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# -------------------------------------------------------
# Back Button
# -------------------------------------------------------

def back_button():

    keyboard = [

        [
            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="main_menu"
            )
        ]

    ]

    return InlineKeyboardMarkup(keyboard)



# -------------------------------------------------------
# FAQ Menu
# -------------------------------------------------------

def faq_keyboard(faqs):

    keyboard = []


    for faq in faqs:

        faq_id = faq[0]

        question = faq[1]


        keyboard.append(

            [

                InlineKeyboardButton(
                    question,
                    callback_data=f"faq_{faq_id}"
                )

            ]

        )


    keyboard.append(

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="main_menu"
            )

        ]

    )


    return InlineKeyboardMarkup(keyboard)



# -------------------------------------------------------
# Language Menu
# -------------------------------------------------------

def language_keyboard():

    keyboard = []


    for code, name in SUPPORTED_LANGUAGES.items():

        keyboard.append(

            [

                InlineKeyboardButton(
                    name,
                    callback_data=f"lang_{code}"
                )

            ]

        )


    keyboard.append(

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="main_menu"
            )

        ]

    )


    return InlineKeyboardMarkup(keyboard)



# -------------------------------------------------------
# Admin Menu
# -------------------------------------------------------

def admin_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "📊 Statistics",
                callback_data="admin_stats"
            )

        ],

        [

            InlineKeyboardButton(
                "📢 Broadcast",
                callback_data="admin_broadcast"
            )

        ],

        [

            InlineKeyboardButton(
                "❓ Manage FAQ",
                callback_data="admin_faq"
            )

        ],

        [

            InlineKeyboardButton(
                "⬅️ Exit",
                callback_data="main_menu"
            )

        ]

    ]


    return InlineKeyboardMarkup(keyboard)



# -------------------------------------------------------
# Educational Information Menu
# -------------------------------------------------------

def guides_keyboard():

    keyboard = [

        [

            InlineKeyboardButton(
                "📈 Market Analysis",
                callback_data="market_analysis"
            )

        ],

        [

            InlineKeyboardButton(
                "⚙️ Trading Automation",
                callback_data="automation"
            )

        ],

        [

            InlineKeyboardButton(
                "🛡 Risk Management",
                callback_data="risk_management"
            )

        ],

        [

            InlineKeyboardButton(
                "📖 Strategy Development",
                callback_data="strategy"
            )

        ],

        [

            InlineKeyboardButton(
                "⬅️ Back",
                callback_data="main_menu"
            )

        ]

    ]


    return InlineKeyboardMarkup(keyboard)
