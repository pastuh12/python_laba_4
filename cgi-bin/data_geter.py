import sqlite3

def take_brokers_data():
    try:
        con = sqlite3.connect('./bd/database.db')
        cur = con.cursor()
        cur.execute('SELECT id, title FROM brokers')
        rows = cur.fetchall()
    except Exception as error:
        print(error)
        rows = []
    finally:
        return rows


def take_users_data():
    try:
        con = sqlite3.connect('./bd/database.db')
        cur = con.cursor()
        cur.execute('SELECT id, name FROM users')
        rows = cur.fetchall()
    except Exception as error:
        print(error)
        rows = []
    finally:
        return rows
