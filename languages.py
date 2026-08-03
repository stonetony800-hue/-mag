"""
=========================================================
AlgoPipX Educational Assistant
Language Manager
=========================================================
"""


# -------------------------------------------------------
# English
# -------------------------------------------------------

ENGLISH = {

    "welcome":
        (
            "👋 Welcome to AlgoPipX Educational Assistant!\n\n"

            "This assistant provides educational resources about:\n\n"

            "• Algorithmic Trading\n"
            "• XAUUSD (Gold)\n"
            "• Deriv Synthetic Indices\n"
            "• Market Analysis\n"
            "• Trading Automation\n"
            "• Risk Management\n"
            "• Strategy Development\n\n"

            "📚 All information is for educational purposes only "
            "and is not financial or investment advice.\n\n"

            "Select an option below:"
        ),


    "guides":
        (
            "📚 Educational Guides\n\n"

            "Choose a topic to learn more:"
        ),


    "market_analysis":
        (
            "📈 Market Analysis\n\n"

            "Learn about analysing market structure, "
            "price movement, and technical concepts."
        ),


    "automation":
        (
            "⚙️ Trading Automation\n\n"

            "Learn about algorithmic trading concepts, "
            "automation tools, and strategy development."
        ),


    "risk_management":
        (
            "🛡 Risk Management\n\n"

            "Understand the importance of managing risk "
            "when studying trading systems."
        ),


    "strategy":
        (
            "📖 Strategy Development\n\n"

            "Explore how trading strategies are researched, "
            "tested, and improved."
        ),


    "about":
        (
            "ℹ️ About AlgoPipX\n\n"

            "AlgoPipX Educational Assistant provides "
            "learning resources about algorithmic trading "
            "and market education.\n\n"

            "This platform is for educational purposes only."
        ),


    "faq_empty":
        (
            "❓ No FAQs are available yet."
        ),


    "language_changed":
        (
            "✅ Language updated successfully."
        )

}



# -------------------------------------------------------
# Kiswahili
# -------------------------------------------------------

SWAHILI = {


    "welcome":
        (
            "👋 Karibu kwenye AlgoPipX Educational Assistant!\n\n"

            "Msaidizi huyu hutoa elimu kuhusu:\n\n"

            "• Algorithmic Trading\n"
            "• XAUUSD (Gold)\n"
            "• Deriv Synthetic Indices\n"
            "• Uchambuzi wa Soko\n"
            "• Automation ya Trading\n"
            "• Usimamizi wa Hatari\n"
            "• Uundaji wa Mikakati\n\n"

            "📚 Taarifa zote ni kwa madhumuni ya elimu "
            "pekee na sio ushauri wa kifedha au uwekezaji."
        ),


    "guides":
        (
            "📚 Miongozo ya Elimu\n\n"

            "Chagua mada unayotaka kujifunza:"
        ),


    "market_analysis":
        (
            "📈 Uchambuzi wa Soko\n\n"

            "Jifunze kuhusu uchambuzi wa mwenendo wa soko "
            "na dhana za bei."
        ),


    "automation":
        (
            "⚙️ Automation ya Trading\n\n"

            "Jifunze kuhusu mifumo ya trading na "
            "maendeleo ya mikakati."
        ),


    "risk_management":
        (
            "🛡 Usimamizi wa Hatari\n\n"

            "Elewa umuhimu wa kudhibiti hatari "
            "katika mifumo ya trading."
        ),


    "strategy":
        (
            "📖 Uundaji wa Mikakati\n\n"

            "Jifunze jinsi mikakati inavyotafitiwa "
            "na kuboreshwa."
        ),


    "about":
        (
            "ℹ️ Kuhusu AlgoPipX\n\n"

            "AlgoPipX Educational Assistant hutoa "
            "elimu kuhusu algorithmic trading."
        ),


    "faq_empty":
        (
            "❓ Hakuna FAQ kwa sasa."
        ),


    "language_changed":
        (
            "✅ Lugha imebadilishwa."
        )

}



# -------------------------------------------------------
# Language Selector
# -------------------------------------------------------

LANGUAGES = {

    "en": ENGLISH,

    "sw": SWAHILI

}



def get_text(language, key):

    if language in LANGUAGES:

        return LANGUAGES[language].get(
            key,
            ENGLISH.get(key, "")
        )


    return ENGLISH.get(key, "")
