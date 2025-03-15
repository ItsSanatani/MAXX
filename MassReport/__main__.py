from pyrogram import idle
from MassReport.main import app
from MassReport.module import start, help, ping, report, join, session

if __name__ == "__main__":
    print("Bot is starting...")
    app.start()
    print("Bot is running!")
    idle()
    print("Bot is stopping...")
    app.stop()
