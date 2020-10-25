import sqlite3

connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE todo_list(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        todos VARCHAR(100)
    );"""

)

connection.commit()
cursor.close()
connection.close()