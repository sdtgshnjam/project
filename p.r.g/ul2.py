import sqlite3
import time 
import requests
# u know bro this is a to project to my  dream
# i love this project so much
#إنشاء إتصال بقاعدة البيانات 
conn = sqlite3.connect('quotes.db')
cur = conn.cursor()
#إنشاء جدول لتخزين الاقتباسات

cur.execute('''
            CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT NOT NULL,
    author TEXT NOT NULL
            )
            
           ''')
conn.commit()
#دالة لجلب اقتابس 
def get_quote():
    url =  "https://api.quotable.io/random" #API 
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return data["content"], data["author"]
    return None
#دالة لتحميل الاقتباسات
def save_quote_to_db(quote, author):
    cur.execute(''' INSERT INTO quotes (quote, author) VALUES (?, ?)''', (quote, author)) 
    conn.commit()
for i in range(5):
    print(f"يتم تحميل الأقتباس {i+1}...")
    quote, author = get_quote()
    if quote and author:
        save_quote_to_db(quote, author)
        time.sleep(1)
print("\n📚 الاقتباسات المخزنة في قاعدة البيانات:")
cur.execute('SELECT * FROM quotes')
rows = cur.fetchall()
for row in rows:
    print(f"{row[0]}. \"{row[1]}\" — {row[2]}")
conn.close()

#المشروع الاول او الثاني