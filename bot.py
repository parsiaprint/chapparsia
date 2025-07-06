import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

# راه اندازی لاگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# پیام خوشامد و منوی اصلی
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🖨 چاپ جزوه", callback_data="print_booklet")],
        [InlineKeyboardButton("💳 کارت ویزیت", callback_data="business_card")],
        [InlineKeyboardButton("📄 تراکت", callback_data="tract")],
        [InlineKeyboardButton("📑 سربرگ", callback_data="letterhead")],
        [InlineKeyboardButton("📢 بنر", callback_data="banner")],
        [InlineKeyboardButton("🎟 استیکر", callback_data="sticker")],
        [InlineKeyboardButton("🏷 لیبل", callback_data="label")],
        [InlineKeyboardButton("🎨 طراحی", callback_data="design")],
        [InlineKeyboardButton("✨ فرم حرفه‌ای سفارش", web_app=WebAppInfo(url="https://your-deployed-webapp-url.com"))],
        [InlineKeyboardButton("📞 پشتیبانی فوری ☎️", callback_data="support")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 خوش آمدید به چاپ پارسیا! لطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup)

# مدیریت دکمه‌ها
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "print_booklet":
        keyboard = [
            [InlineKeyboardButton("⚫️ سیاه و سفید", callback_data="bw")],
            [InlineKeyboardButton("🌈 رنگی", callback_data="color")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="main_menu")]
        ]
        await query.edit_message_text("لطفاً نوع چاپ را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "bw":
        keyboard = [
            [InlineKeyboardButton("📚 تعداد زیاد (بالای ۵۰ برگ)", callback_data="bw_many")],
            [InlineKeyboardButton("📄 تعداد کم (زیر ۵۰ برگ)", callback_data="bw_few")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="print_booklet")]
        ]
        await query.edit_message_text("لطفاً تعداد را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data in ["bw_many", "bw_few", "color_many", "color_few"]:
        keyboard = [
            [InlineKeyboardButton("🔘 یکرو", callback_data="send_file")],
            [InlineKeyboardButton("🔄 پشت و رو", callback_data="send_file")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="bw" if "bw" in data else "color")]
        ]
        await query.edit_message_text("تک رو یا پشت و رو؟", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "color":
        keyboard = [
            [InlineKeyboardButton("📚 تعداد زیاد (بالای ۵۰ برگ)", callback_data="color_many")],
            [InlineKeyboardButton("📄 تعداد کم (زیر ۵۰ برگ)", callback_data="color_few")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="print_booklet")]
        ]
        await query.edit_message_text("لطفاً تعداد را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "send_file":
        await query.edit_message_text("لطفاً فایل خود را ارسال کنید 📎")

    elif data == "main_menu":
        await start(update, context)

    elif data == "business_card":
        keyboard = [
            [InlineKeyboardButton("💼 ساده", callback_data="bc_simple")],
            [InlineKeyboardButton("🏅 حرفه‌ای", callback_data="bc_pro")],
            [InlineKeyboardButton("👑 لاکچری", callback_data="bc_lux")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="main_menu")]
        ]
        await query.edit_message_text("لطفاً نوع کارت ویزیت را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "bc_simple":
        keyboard = [
            [InlineKeyboardButton("سلفون معمولی یکرو", callback_data="send_file")],
            [InlineKeyboardButton("سلفون معمولی دورو", callback_data="send_file")],
            [InlineKeyboardButton("گوشه گرد یکرو", callback_data="send_file")],
            [InlineKeyboardButton("گوشه گرد دورو", callback_data="send_file")],
            [InlineKeyboardButton("مربعی دورو", callback_data="send_file")],
            [InlineKeyboardButton("دایره‌ای دورو", callback_data="send_file")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="business_card")]
        ]
        await query.edit_message_text("نوع کارت ویزیت ساده را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "bc_pro":
        keyboard = [
            [InlineKeyboardButton("لمینت براق دورو", callback_data="send_file")],
            [InlineKeyboardButton("لمینت مات دورو", callback_data="send_file")],
            [InlineKeyboardButton("لمینت برجسته دورو", callback_data="send_file")],
            [InlineKeyboardButton("لمینت مربعی دورو", callback_data="send_file")],
            [InlineKeyboardButton("برجسته مربعی دورو", callback_data="send_file")],
            [InlineKeyboardButton("مخملی مربعی", callback_data="send_file")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="business_card")]
        ]
        await query.edit_message_text("نوع کارت حرفه‌ای را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "bc_lux":
        keyboard = [
            [InlineKeyboardButton("لمینت طلاکوب", callback_data="send_file")],
            [InlineKeyboardButton("برجسته طلاکوب", callback_data="send_file")],
            [InlineKeyboardButton("PVC", callback_data="send_file")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="business_card")]
        ]
        await query.edit_message_text("نوع کارت لاکچری را انتخاب کنید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data in ["tract", "letterhead", "banner", "sticker", "label", "design"]:
        keyboard = [
            [InlineKeyboardButton("📎 ارسال فایل", callback_data="send_file")],
            [InlineKeyboardButton("🔙 بازگشت", callback_data="main_menu")]
        ]
        await query.edit_message_text("لطفاً فایل خود را ارسال نمایید:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "support":
        await query.edit_message_text("❗️در صورتی که ربات پاسخگوی نیاز شما نبود و موضوع فوری است با شماره 09177037793 تماس بگیرید یا در تلگرام پیام دهید. لطفاً در غیر این صورت از تماس خودداری فرمایید.")

# دریافت فایل و ارسال به گروه
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    user = update.message.from_user

    caption = (
        f"📥 فایل جدید دریافت شد:\n"
        f"👤 نام: {user.full_name}\n"
        f"🆔 یوزرنیم: @{user.username if user.username else 'ندارد'}\n"
        f"📎 نام فایل: {document.file_name}"
    )

    # ارسال فایل به گروه
    await context.bot.send_document(
        chat_id=610732951,
        document=document.file_id,
        caption=caption
    )

    # پاسخ به کاربر
    await update.message.reply_text("فایل دریافت شد ✅\nسفارش شما بررسی خواهد شد.")

# شروع برنامه
def main():
    TOKEN = "7296058262:AAH8kz4p579M0vZC6yBeTxWCi6FiHWfjC0w"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
