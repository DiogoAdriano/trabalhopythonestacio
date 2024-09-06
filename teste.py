import sqlite3

def check_table_structure():
    conn = sqlite3.connect('escola.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info(alunos)")
    columns = c.fetchall()
    conn.close()

    for column in columns:
        print(column)

check_table_structure()