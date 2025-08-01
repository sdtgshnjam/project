import os
import uuid
import telebot
from yt_dlp import YoutubeDL

# توكن البوت
BOT_TOKEN = "7637862024:AAGpsarkSgXCzRFymjcujyq6G2fVPikvnBE"

bot = telebot.TeleBot(BOT_TOKEN)

DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "أرسل رابط فيديو تيك توك أو إنستغرام لتحميله.")

@bot.message_handler(func=lambda m: m.text.startswith("http"))
def download_video(msg):
    url = msg.text.strip()

    if not ("tiktok.com" in url or "instagram.com" in url):
        bot.reply_to(msg, "هذا الرابط غير مدعوم. أرسل فقط من تيك توك أو إنستغرام.")
        return

    ydl_opts = {
        'format': 'bestvideo*+bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s')
    }

    try:
        bot.reply_to(msg, "⏳ جاري التحميل...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as video:
            bot.send_video(msg.chat.id, video, timeout=120)

    except Exception as e:
        bot.reply_to(msg, f"❌ خطأ: {e}")

    finally:
        if 'filename' in locals() and os.path.exists(filename):
            os.remove(filename)

bot.polling(none_stop=True)
