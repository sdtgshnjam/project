import telebot
from note_bot import Notebot

TOKEN = "7957705378:AAG6Cl3sUZ2C0OnY8APKCpGk7joKZdHUke0"
bot = telebot.TeleBot(TOKEN)

notebot = Notebot()  #هنا نستخدم الكلاس من الملف 

@bot.message_handler(commands=['start'])
def start(message):
    
    bot.reply_to(message, "مرحبا أنا الملاحظ \n هنا ملاحظاتك الشخصية و مهامك الخاصة\n انا اعتبر احد المشاريع التي لا تصحى من المطور صلاح |ليل", )


@bot.message_handler(commands=['add'])
def add_note(message):
    user_id = message.from_user.id
    note = message.text[5:] #لم افهم ليه رقم 5

    if not note:
        bot.reply_to(message, "الرجاء إدخال ملاحظتك بعد  الامر \n /add")
        return
    notebot.add_notes(user_id, note)
    bot.reply_to(message, "تم إضافة الملاحظة !")

@bot.message_handler(commands=['list'])

def list_notes(message):
    user_id = message.from_user.id
    notes = notebot.list_notes(user_id)
    if not notes:
        bot.reply_to(message, f"لا توجد ملاحظة الرجاء كتابة ملاحظة. \n /add")
        return
    response = "\n".join([f"{n[0]}. {n[1]} ({n[2]})" for n in notes])
    bot.reply_to(message, response)


@bot.message_handler(commands=['delete'])

def delete_note(message):
    args = message.text.split()
    
    if len(args) != 2 or not args[1].isdigit():
        bot.reply_to(message, "الرجاء إدخال رقم الملاحظة بعد الامر \n /delete ")

        return
    note_id = int(args[1])
    notebot.delete_note(message.from_user.id, note_id)
    bot.reply_to(message, "🗑️ تم حذف الملاحظة!")

@bot.message_handler(commands=['search'])
def search_notes(message):
    keyword = message.text[8:].strip()  #لم افهم ليه رقم 
    if not keyword:
        bot.reply_to(message, "❗️اكتب كلمة للبحث بعدها")
        return
    results = notebot.search_notes(message.from_user.id, keyword)
    if results:
        response = "\n".join([f"{r[0]}. {r[1]}" for r in results])
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "🔍 لا توجد نتائج.")

bot.polling()




