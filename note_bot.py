import sqlite3

class Notebot:
    def __init__(self, db_name='notes.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def add_notes(self, user_id, note):
        self.c.execute(''' INSERT INTO notes (user_id, note) VALUES (?, ?) ''', (user_id, note))
        self.conn.commit()

    def list_notes(self, user_id):
        self.c.execute(''' SELECT id, note, timestamp FROM notes WHERE user_id = ? ''', (user_id,))
        return self.c.fetchall() #ليه كذا؟؟
    
    def delete_note(self, note_id, user_id):
        self.c.execute(''' DELETE FROM notes WHERE id = ? AND user_id = ? ''', (note_id, user_id))
        self.conn.commit()

    def search_notes(self, keyword, user_id):
        self.c.execute(''' SELECT id, note FROM notes WHERE user_id = ? AND note LIKE ? ''', (user_id, f'%{keyword}%')) #لم افهم هذا السطر بصرتاحة
        return self.c.fetchall()
        #LIKE يستخدم للبحث عن النصوص
        #% معناها "أي شيء قبل أو بعد الكلمة".
        