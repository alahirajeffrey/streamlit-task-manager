import sqlite3

def create_connection():
    try:
        connection = sqlite3.connect('tasks.db')
        return connection
    except Exception as e:
        return e