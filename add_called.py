import sqlite3

DB = None
CONN = None

def connect():
    global DB, CONN
    CONN = sqlite3.connect("melons.db")
    DB = CONN.cursor()

def add_called():
    connect()
    query = """ALTER TABLE customers ADD COLUMN called DATE"""
    DB.execute(query)

add_called()