import os
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

def send_resume(update, context):
    chat_id = update.message.chat_id
    with open("resume.pdf", "rb") as file:
        context.bot.send_document(chat_id=chat_id, document=InputFile(file), filename="Pavan_Resume.pdf")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("resume", send_resume))
updater.start_polling()
updater.idle()
