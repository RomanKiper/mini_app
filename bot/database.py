import sqlite3
from bot.config import DB_PATH

def init_db():
    """Создание таблицы, если её нет"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_message(user_id, message, response):
    """Сохранение сообщения и ответа в базу данных"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (user_id, message, response) VALUES (?, ?, ?)',
                   (user_id, message, response))
    conn.commit()
    conn.close()
