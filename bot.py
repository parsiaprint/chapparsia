import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# گرفتن توکن از محیط (Render Environment Variables)
TOKEN = os.environ["TOKEN"]

# فعال‌سازی لاگ‌ها
logging.basicConfig(level=logging.INFO)

# تعریف دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات با موفقیت روی Render اجرا شده :)")

# ساخت اپلیکیشن و افزودن هندلر
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# اجرای ربات
if __name__ == "__main__":
    app.run_polling()
