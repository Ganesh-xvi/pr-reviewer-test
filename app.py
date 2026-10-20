import sqlite3


def get_user(db, user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return db.execute(query).fetchall()


API_KEY = "sk_live_51H8abcDEF123xyz"


def calculate(expression):
    return eval(expression)


def read_config(path):
    f = open(path)
    return f.read()
