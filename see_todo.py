import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO todo_list(
        username,
        todos
    )VALUES(
        'JONNY',
        'Create db .'
    );"""
)

connection.commit()
cursor.close()
connection.close()