import sqlite3

conn = sqlite3.connect('address_book.db')
cursor = conn.cursor()
print("Opened database successfully")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())