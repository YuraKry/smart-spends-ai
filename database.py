import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses 
                 (id INTEGER PRIMARY KEY, amount REAL, category TEXT, comment TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_expense(amount, category, comment):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, comment) VALUES (?, ?, ?)", (amount, category, comment))
    conn.commit()
    conn.close()
    return f"Записано: {amount} грн на {category} ({comment})"


def get_all_expenses():
    conn = sqlite3.connect('finance.db')
    # Читаємо дані
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df.to_dict(orient='records')