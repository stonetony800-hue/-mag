"""
=========================================================
AlgoPipX Educational Assistant
Configuration File
=========================================================
"""

import os

# -------------------------------------------------------
# Telegram
# -------------------------------------------------------

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")

PORT = int(os.getenv("PORT", "8080"))

# -------------------------------------------------------
# Bot Information
# -------------------------------------------------------

BOT_NAME = "AlgoPipX Educational Assistant"

BOT_VERSION = "2.0.0"

BOT_DESCRIPTION = (
    "Educational content on algorithmic trading for "
    "XAUUSD (Gold) and Deriv Synthetic Indices."
)

# -------------------------------------------------------
# Admin
# -------------------------------------------------------
# Replace with your Telegram numeric User ID
# Example:
# ADMIN_IDS = [123456789]

ADMIN_IDS = [
    int(x)
    for x in os.getenv("ADMIN_IDS", "").split(",")
    if x.strip()
]

# -------------------------------------------------------
# Channel
# -------------------------------------------------------

CHANNEL_USERNAME = "@AlgoPipX_Robots"

CHANNEL_LINK = "https://t.me/AlgoPipX_Robots"

# -------------------------------------------------------
# Support
# -------------------------------------------------------

SUPPORT_USERNAME = "@algopipxhft"

# -------------------------------------------------------
# Languages
# -------------------------------------------------------

DEFAULT_LANGUAGE = "en"

SUPPORTED_LANGUAGES = {
    "en": "🇬🇧 English",
    "sw": "🇹🇿 Kiswahili"
}

# -------------------------------------------------------
# Database
# -------------------------------------------------------

DATABASE_NAME = "algopipx.db"

FAQ_FILE = "faq.json"

# -------------------------------------------------------
# Broadcast
# -------------------------------------------------------

BROADCAST_DELAY = 0.05

# -------------------------------------------------------
# Logging
# -------------------------------------------------------

LOG_LEVEL = "INFO"

# -------------------------------------------------------
# Disclaimer
# -------------------------------------------------------

DISCLAIMER = (
    "This bot provides educational information about "
    "algorithmic trading.\n\n"
    "Nothing contained here should be considered "
    "financial, investment, or trading advice."
)

# -------------------------------------------------------
# Welcome Message
# -------------------------------------------------------

WELCOME_MESSAGE = (
    "👋 Welcome to AlgoPipX Educational Assistant!\n\n"

    "This assistant provides educational resources on:\n\n"

    "• Algorithmic Trading\n"
    "• XAUUSD (Gold)\n"
    "• Deriv Synthetic Indices\n"
    "• Market Analysis\n"
    "• Trading Automation\n"
    "• Risk Management\n"
    "• Strategy Development\n\n"

    "📚 All information shared is intended solely for "
    "educational purposes.\n\n"

    "Please choose one of the options below."
)
