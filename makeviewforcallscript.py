import sqlite3

DB = None
CONN = None

def connect():
    global DB, CONN
    CONN = sqlite3.connect("melons.db")
    DB = CONN.cursor()

def makeview():
    connect()
    query = """CREATE VIEW custstocall AS SELECT customers.id, givenname, surname, telephone, called, order_total FROM customers JOIN orders ON customers.id = orders.customer_id WHERE customers.called is null"""
    DB.execute(query)
    CONN.commit()

makeview()