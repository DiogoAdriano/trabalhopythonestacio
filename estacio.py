import sqlite3

def init_db():
    conn = sqlite3.connect('escola.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            confirmado BOOLEAN NOT NULL,
            pago BOOLEAN NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
