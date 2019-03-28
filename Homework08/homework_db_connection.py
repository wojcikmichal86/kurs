import sqlite3

with sqlite3.connect('homework.db') as connection:
    connection.row_factory = sqlite3.Row
    db_cursor = connection.cursor()
    print(db_cursor)