from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

HELP_TEXT = """
📖 **Help Menu** 📖

🔹 `/start` - Start the bot
🔹 `/addsession <session_string>` - Add a session string
🔹 `/mysession` - View your added sessions
🔹 `/rmsession <session_id>` - Remove a session
🔹 `/report` - Report a message

📌 **How to use Report Command?**  
1️⃣ Use `/report` and follow the instructions  
2️⃣ Provide the group/channel link  
3️⃣ Provide the message link  
4️⃣ Select the reason for the report  
5️⃣ Enter the number of reports to send  

⚠️ **Only the owner can use this bot.**
"""

@Client.on_message(filters.command("help") & filters.user(OWNER_ID))
async def help_command(client: Client, message: Message):
    buttons = [
        [InlineKeyboardButton("🔙 Back", callback_data="start_menu")]
    ]
    
    await message.reply_text(
        HELP_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )
