import os
import logging
from aiohttp import web
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration from environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g., https://your-subdomain.onrender.com
PORT = int(os.getenv("PORT", 8080))

# Sample Compliant Music Data (Simulating a legal, curated preview database)
MUSIC_DATABASE = {
    "ambient": [
        {"id": "amb_1", "title": "Lo-Fi Focus Beat", "artist": "Veloce Audio", "duration": "02:30"},
        {"id": "amb_2", "title": "Deep Space Drone", "artist": "Synth Wave", "duration": "04:15"}
    ],
    "energetic": [
        {"id": "eng_1", "title": "Neon Horizon", "artist": "Cyber Drift", "duration": "03:10"},
        {"id": "eng_2", "title": "Tech Pulse", "artist": "Digital Core", "duration": "02:45"}
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Compliant Welcome Screen with distinct Clear Call to Actions."""
    user = update.effective_user
    text = (
        f"Hello {user.first_name}! Welcome to the Curated Music Discovery Assistant.\n\n"
        "Explore copyright-compliant tracks, sort by mood, and organize your royalty-free playlists seamlessly. "
        "All functionalities adhere entirely to Telegram Developer Policies."
    )
    
    keyboard = [
        [
            InlineKeyboardButton("🎵 Browse by Mood", callback_data="browse_moods"),
            InlineKeyboardButton("ℹ️ About & Terms", callback_data="about_info")
        ],
        [InlineKeyboardButton("❓ How to Use / Help", callback_data="help_info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup)

async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Explicit help guidelines required by manual ad moderators."""
    text = (
        "💡 **How to navigate this Assistant:**\n\n"
        "1. Tap 'Browse by Mood' to view curated genres.\n"
        "2. Select any track to preview production details.\n"
        "3. Use /browse or /about to navigate directly via commands.\n\n"
        "For additional support or complaints regarding content licensing, please contact our team via standard support channels."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")]]
    await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Required policy/developer transparency text."""
    text = (
        "🏛 **About Curated Music Discovery**\n\n"
        "This application serves as an index for royalty-free audio tracks intended for background use in creator content. "
        "We respect copyright ownership. If you believe your rights are infringed, use our formal takedown channels.\n\n"
        "**Version:** 1.0.0 (Production)\n"
        "**Host Environment:** Verified Cloud Architecture"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")]]
    await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def browse_moods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays category selection."""
    text = "Select an audio mood to filter tracks:"
    keyboard = [
        [InlineKeyboardButton("🧘 Ambient / Lo-Fi", callback_data="mood_ambient")],
        [InlineKeyboardButton("⚡ Energetic / Electronic", callback_data="mood_energetic")],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")]
    ]
    await update.callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def list_tracks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Lists matching library items."""
    query = update.callback_query
    mood = query.data.split("_")[1]
    tracks = MUSIC_DATABASE.get(mood, [])
    
    text = f"✨ Showing tracks matching [{mood.upper()}]:"
    keyboard = []
    
    for t in tracks:
        keyboard.append([InlineKeyboardButton(f"▪️ {t['title']} ({t['duration']})", callback_data=f"track_{mood}_{t['id']}")])
        
    keyboard.append([InlineKeyboardButton("⬅️ Change Mood", callback_data="browse_moods")])
    await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def track_details(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays details without providing pirated download paths."""
    query = update.callback_query
    _, mood, track_id = query.data.split("_")
    
    tracks = MUSIC_DATABASE.get(mood, [])
    track = next((t for t in tracks if t["id"] == track_id), None)
    
    if not track:
        await query.answer("Track data no longer available.")
        return

    text = (
        f"🎵 **Track Profile**\n\n"
        f"🗂 **Title:** {track['title']}\n"
        f"🎙 **Artist:** {track['artist']}\n"
        f"⏱ **Length:** {track['duration']}\n"
        f"⚖️ **License:** Creative Commons (Attribution Required)"
    )
    
    keyboard = [
        [InlineKeyboardButton("🎧 Request Audition Stream", callback_data="stream_mock")],
        [InlineKeyboardButton("⬅️ Back to List", callback_data=f"mood_{mood}")]
    ]
    await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def stream_mock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Streaming initialization requested... (Demo Only)", show_alert=True)

# --- WEB SERVER INTERFACE FOR RENDER ---

async def handle_webhook(request):
    """Processes inbound payloads from Telegram via webhook."""
    app = request.app['bot_app']
    body = await request.json()
    update = Update.de_json(body, app.bot)
    await app.process_update(update)
    return web.Response(status=200)

async def handle_health(request):
    """Vital endpoint preventing Render deployment timeout failures."""
    return web.Response(text="Bot Status: Operational & Fully Compliant", status=200)

async def on_startup(app_web):
    """Executed automatically when the web application boots up."""
    if not TOKEN or not WEBHOOK_URL:
        logger.error("Environment variables 'TELEGRAM_TOKEN' and 'WEBHOOK_URL' are missing.")
        raise ValueError("Missing critical environment setup.")

    # Initialize Bot Application Architecture
    bot_app = Application.builder().token(TOKEN).build()

    # Route Assignments
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("browse", browse_moods))
    bot_app.add_handler(CommandHandler("about", start))
    bot_app.add_handler(CallbackQueryHandler(start, pattern="main_menu"))
    bot_app.add_handler(CallbackQueryHandler(handle_help, pattern="help_info"))
    bot_app.add_handler(CallbackQueryHandler(handle_about, pattern="about_info"))
    bot_app.add_handler(CallbackQueryHandler(browse_moods, pattern="browse_moods"))
    bot_app.add_handler(CallbackQueryHandler(list_tracks, pattern="mood_"))
    bot_app.add_handler(CallbackQueryHandler(track_details, pattern="track_"))
    bot_app.add_handler(CallbackQueryHandler(stream_mock, pattern="stream_mock"))

    await bot_app.initialize()
    await bot_app.start()
    
    # Establish precise webhook route link with Telegram API servers
    await bot_app.bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    
    # Save bot instance to reference within requests
    app_web['bot_app'] = bot_app
    logger.info("Telegram Bot architecture successfully linked & operational.")

async def on_cleanup(app_web):
    """Ensures clean task closure during server reloads or stops."""
    bot_app = app_web.get('bot_app')
    if bot_app:
        logger.info("Executing clean shutdown sequencing...")
        await bot_app.stop()
        await bot_app.shutdown()

def main():
    # Setup standard web server container mapping
    web_app = web.Application()
    
    # Bind lifecycles
    web_app.on_startup.append(on_startup)
    web_app.on_cleanup.append(on_cleanup)
    
    # Register paths
    web_app.router.add_post('/webhook', handle_webhook)
    web_app.router.add_get('/', handle_health)
    web_app.router.add_get('/health', handle_health)

    # Run blocking app handler loop (Perfect for Render environment retention)
    web.run_app(web_app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    main()
