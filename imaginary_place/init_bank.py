import sqlite3

def connect():
    conn = sqlite3.connect('imaginary_place/bank.db')
    
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS places (id INTEGER PRIMARY KEY AUTOINCREMENT,author TEXT NOT NULL, description TEXT NOT NULL, text TEXT NOT NULL)")
    
    conn.commit()
    conn.close() 
