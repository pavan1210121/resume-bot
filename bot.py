import os
from telegram.ext import Updater, CommandHandler
from telegram import InputFile
import imghdr  # Corrected import for image header checking

# Make sure the environment variable for BOT_TOKEN is set correctly
BOT_TOKEN = os.getenv("7331766657:AAGPN0eYnryJ7N3BLCUUJZTEtYMXRsNiC34")  # Use the correct environment variable name

def send_resume(update, context):
    chat_id = update.message.chat_id
    with open("resume.pdf", "rb") as file:
        context.bot.send_document(chat_id=chat_id, document=InputFile(file), filename="Pavan_Resume.pdf")

# Create Updater object and set up the command handler
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# Add command handler for /resume command
dp.add_handler(CommandHandler("resume", send_resume))

# Start the bot
updater.start_polling()
updater.idle()
