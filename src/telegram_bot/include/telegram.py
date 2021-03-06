import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def bot_start():
    updater = Updater(os.environ.get("TELEGRAM_TOKEN", ""))

    updater.dispatcher.add_handler(CommandHandler("hello", hello))

    updater.start_polling()
    updater.idle()
