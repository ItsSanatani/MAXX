from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, CHANNEL_USERNAME

@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("🚀 Start Mass Report", callback_data="start_mass_report")],
        [InlineKeyboardButton("👑 Owner", user_id=OWNER_ID)],
        [InlineKeyboardButton("📢 Channel", url=f"https://t.me/The_Over_Op")],
        [InlineKeyboardButton("📖 Help Menu", callback_data="help_menu")]
    ]
    
    await client.send_message(
        OWNER_ID,
        "👋 Welcome to Mass Report Bot!\n\nUse this bot to report messages in groups/channels.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
