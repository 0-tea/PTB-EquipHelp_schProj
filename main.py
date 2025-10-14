""" Базовый минимум: """
from datetime import datetime
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

""" Коги: """
from utils.bot_info import bot_info

try:
    BOT_TOKEN = open('token.txt').read().strip()
except FileNotFoundError:
    print("Отсутствует токен.")
    exit(12345)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_name = await context.bot.get_my_name()
    user = update.effective_user
    await update.message.reply_text(f"Привет {user.first_name}! \n"
                                    f"Меня зовут {bot_name.name}, буду рад помочь вам разобраться в работе с оборудованием!")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", bot_info))

    application.bot_data['start_time'] = datetime.now()
    print(f"log:    START    {application.bot_data['start_time'].strftime('%H:%M:%S %d.%m.%Y')}")
    application.run_polling()


if __name__ == "__main__":
    main()