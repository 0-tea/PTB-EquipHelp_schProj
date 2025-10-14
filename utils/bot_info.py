from datetime import datetime

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

async def bot_info(update, context: ContextTypes.DEFAULT_TYPE):
    """ Краткое сообщение основное направление, кто делал, справка по боту """
    bot_info = await context.bot.get_me()

    info_text = \
f"""От разработчиков:
    Бот направлен на помощь в освоении оборудования в ИТ классах
    Создали учащиеся школы ГБОУ №508 10Т класса
    Руководством Учителя информатики и куратора МЭИ

Справка по боту:
    Имя: {bot_info.first_name}
    Юз: @{bot_info.username}
    Старт в: {context.bot_data['start_time'].strftime('%H:%M:%S %d.%m.%Y')}
    Время работы: {str(datetime.now() - context.bot_data['start_time'])[:-7]}
"""

    await update.message.reply_text(info_text, parse_mode=None) # 'MarkdownV2' parse_mode это что бы в общем то самое было, ну ты понял это же и так понятно, ты же понял верно ?