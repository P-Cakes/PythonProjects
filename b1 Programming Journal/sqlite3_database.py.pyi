import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        #sqlite3 actually creates the cursor for us here:
        #but best practice is to use cursor
        connection.execute("create table entries (content text, date text);")

