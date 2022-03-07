import sqlite3
from .convert import encrypt

# with sqlite3.connect("main.db") as db:
#     cur = db.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS Users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         username TEXT,
#         password TEXT,
#         profile BLOB,
#         email TEXT
#     )""")

def get_db():
    with sqlite3.connect("main.db") as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM Users")
    return cur.fetchall()


def create_account(username : str, password : str):
    try:
        with sqlite3.connect("main.db") as db:
            cur = db.cursor()
            cur.execute("INSERT INTO Users (username, password) VALUES ('{}', '{}')".format(username, password))
        return True
    except Exception as e:
        print(e)
        return False
    

def change_password(username : str, password : str):
    encrypt(password)
    try:
        with sqlite3.connect("main.db") as db:
            cur = db.cursor()
            cur.execute("UPDATE Users SET password='{}' WHERE username={}".format(password, username))
        return True
    except Exception as e:
        print(e)
        return False

def delete_account(username : str): 
    try:
        with sqlite3.connect("main.db") as db:
            cur = db.cursor()
            cur.execute("DELETE FROM Users WHERE username='{}'".format(username))
        return True
    except Exception as e:
        print(e)
        return False


def get_account(username):
    with sqlite3.connect("main.db") as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM Users WHERE username='{}'".format(username))
    return cur.fetchall()
