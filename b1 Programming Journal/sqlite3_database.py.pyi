import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("create table entries (content text, date text);")

