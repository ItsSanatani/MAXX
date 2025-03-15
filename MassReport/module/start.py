from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

@Client.on_message(filters.command("start") & filters.user(OWNER_ID))
async def start_command(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("🚀 Start Mass Report", callback_data="start_report")],
        [InlineKeyboardButton("👑 Owner", user_id=OWNER_ID), InlineKeyboardButton("📢 Channel", url="https://t.me/The_Over_Op")],
        [InlineKeyboardButton("❓ Help Menu", callback_data="help_menu")]
    ]
    
    await message.reply_text(
        "👋 **Welcome to Mass Report Bot!**\n\nUse the buttons below to navigate.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("help_menu"))
async def help_menu_callback(client, callback_query):
    from MassReport.module.help import HELP_TEXT  # Importing help text

    buttons = [
        [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
    ]

    await callback_query.message.edit_text(
        HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("start_menu"))
async def start_menu_callback(client, callback_query):
    buttons = [
        [InlineKeyboardButton("🚀 Start Mass Report", callback_data="start_report")],
        [InlineKeyboardButton("👑 Owner", user_id=OWNER_ID), InlineKeyboardButton("📢 Channel", url="https://t.me/your_channel")],
        [InlineKeyboardButton("❓ Help Menu", callback_data="help_menu")]
    ]
    
    await callback_query.message.edit_text(
        "👋 **Welcome back to Mass Report Bot!**",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
