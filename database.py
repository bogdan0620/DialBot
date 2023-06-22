import sqlite3
import datetime as dt

connection = sqlite3.connect('users.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users ('
            'input_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'tg_id INTEGER,'
            'weight_up_to REAL,'
            'weight_after REAL,'
            'output REAL,'
            'datetime TEXT);')


def add_weight_up_to_db(tg_id, weight_up_to, datetime):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user1 = sql.execute('SELECT datetime, input_id FROM users WHERE tg_id=?;', (tg_id, )).fetchall()
    input_id = user1[-1][-1]
    if user1:
        if user1[-1][0] == str(dt.date.today()):
            sql.execute('UPDATE users SET weight_up_to=? WHERE tg_id=? AND datetime=? AND input_id=?;', (weight_up_to, tg_id, dt.date.today(), input_id))
            connection.commit()
        else:
            sql.execute('INSERT INTO users (tg_id, weight_up_to, datetime) VALUES (?,?,?);',
                        (tg_id, weight_up_to, datetime))
            connection.commit()
    else:
        sql.execute('INSERT INTO users (tg_id, weight_up_to, datetime) VALUES (?,?,?);', (tg_id, weight_up_to, datetime))
        connection.commit()


def add_weight_after_db(tg_id, weight_after, datetime):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user1 = sql.execute('SELECT datetime, input_id FROM users WHERE tg_id=?;', (tg_id,)).fetchall()
    input_id = user1[-1][-1]
    if user1:
        if user1[-1][0] == str(dt.date.today()):
            sql.execute('UPDATE users SET weight_after=? WHERE tg_id=? AND datetime=? AND input_id=?;', (weight_after, tg_id, dt.date.today(), input_id))
            connection.commit()
        else:
            sql.execute('INSERT INTO users (tg_id, weight_after, datetime) VALUES (?,?,?);',
                        (tg_id, weight_after, datetime))
            connection.commit()
    else:
        sql.execute('INSERT INTO users (tg_id, weight_after, datetime) VALUES (?,?,?);', (tg_id, weight_after, datetime))
        connection.commit()
