import sqlite3

def connect():
    return sqlite3.connect("messages.db")

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(message):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (?)", (message,))
    conn.commit()
    conn.close()

# Create the table automatically
create_table()
