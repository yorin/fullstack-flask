import sqlite3, sys

def show_color(username):
    connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT favorite_color FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    color = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    message = '{username}\'s favorite color is {color}.'.format(username=username, color=color)    
    return message

def fetch_all(username):
    connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    #print (username, file=sys.stderr)
    cursor.execute("""SELECT * FROM todo_list WHERE username='{username}';""".format(username=username))
    fetch_all_data = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    message = fetch_all_data    
    return message

def check_pw(username):
    connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    passwd = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return passwd

def check_users(username):
    connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        Person = db_users[i][0]
        users.append(Person)

    connection.commit()
    cursor.close()
    connection.close()
    return users

def signup(username, password):
    connection = sqlite3.connect ('flask_tut.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username='{username}' ORDER BY pk DESC;""".format(username=username))
    exist = cursor.fetchone()
    #connection.commit()
    #cursor.close()
    #connection.close()

    if exist is None:
        cursor.execute("""INSERT INTO users(username, password) VALUES('{username}', '{password}');""".format(username=username, password=password))
        connection.commit()
        cursor.close()
        connection.close()
        message ='Thank you for signing up!!!'
        return message
    else:
        return ('User already exists')

    return ('You have successfully signed up!!!')

