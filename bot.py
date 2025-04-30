import os
import requests
from telegram import Update, File
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لطفاً فایل بفرست تا لینک دانلود دریافت کنی.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.audio or update.message.photo[-1]
    tg_file: File = await file.get_file()
    file_path = f"temp_{update.message.message_id}"
    await tg_file.download_to_drive(file_path)

    with open(file_path, "rb") as f:
        response = requests.post("https://store1.gofile.io/uploadFile", files={"file": f})

    os.remove(file_path)

    if response.status_code == 200:
        download_link = response.json()["data"]["downloadPage"]
        await update.message.reply_text("آپلود شد! لینک در پیام بعدی ارسال می‌شود.")
        await update.message.reply_text(download_link)
    else:
        await update.message.reply_text("خطا در آپلود فایل.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO | filters.AUDIO | filters.PHOTO, handle_file))
app.run_polling()
