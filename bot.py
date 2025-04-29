import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes

BOT_TOKEN = "7770618048:AAFo3YrHvPKOa8MgtsynrFJFO_xWx7kqrwk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! فایل یا پیام بفرست تا پردازش کنم.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("فایلت دریافت شد! (فعلاً ذخیره سازی نداریم)")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_file))

    await app.initialize()   # اضافه شد
    await app.start()
    await app.updater.start_polling()
    await app.idle()
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
