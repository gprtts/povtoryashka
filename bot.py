import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем .env
load_dotenv()

# Получаем токен из .env
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден! Проверь .env файл и переменную BOT_TOKEN")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я повторяшка. Пиши что угодно — я повторю!")

# Повторялка (текст + медиа через копирование)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Если текст — повторяем текстом
    if update.message.text:
        await update.message.reply_text(update.message.text)
    else:
        # Иначе — копируем (фото, стикеры, голос, видео и т.д.)
        await update.message.copy(update.message.chat_id)

# Главная функция
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, echo))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()