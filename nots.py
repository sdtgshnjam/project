import sqlite3

conn = sqlite3.connect('notes.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS notes
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER,
          note TEXT NOT NULL,
          timestamp DATETIME DEFAULT CURRENT_TIMESTAMP 
          )''') #timestamp DATETIME DEFAULT CURRENT_TIMESTAMP ما فهمت ليه و ذا بعد INTEGER
#timestamp: اسم العمود.

#DATETIME: نوع البيانات (تاريخ + وقت).

#DEFAULT CURRENT_TIMESTAMP: يعني إذا ما عطيت قيمة، يحط تلقائيًا الوقت الحالي.

# هذا مفيد لأنك تقدر تعرف متى كل ملاحظة تم إنشاؤها دون ما تضيفها يدويًا.
conn.commit()
conn.close()
#جدول للنوت


'''
| الجزء                                          | معناه                                    |
| ---------------------------------------------- | ---------------------------------------- |
| `fetchall()`                                   | جلب كل النتائج على شكل قائمة من التابعات |
| `LIKE %كلمة%`                                  | البحث عن كلمة داخل نص                    |
| `timestamp DATETIME DEFAULT CURRENT_TIMESTAMP` | حفظ وقت إضافة كل ملاحظة تلقائيًا         |
| `INTEGER PRIMARY KEY AUTOINCREMENT`            | توليد id تلقائي لكل ملاحظة               |
'''