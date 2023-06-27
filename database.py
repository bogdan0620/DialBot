import sqlite3
import datetime as dt
import typing

connection = sqlite3.connect('users.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users ('
            'input_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'tg_id INTEGER,'
            'weight_up_to REAL,'
            'weight_after REAL,'
            'output REAL,'
            'datetime TEXT);')


def checker_db(tg_id, datetime):
    user2 = sql.execute('SELECT datetime, input_id, weight_up_to, weight_after FROM users WHERE tg_id=?;', (tg_id,)).fetchall()
    if len(user2) >= 2:
        one: float = user2[-1][-2]
        two: float = user2[-2][-1]
        # output = float(one.replace(',', '.')) - float(two.replace(',', '.'))
        output = one - two
        input_id = user2[-1][-3]
        if user2[-1][0] == str(dt.date.today()):
            sql.execute('UPDATE users SET output=? WHERE tg_id=? AND datetime=? AND input_id=?;', (output, tg_id, dt.date.today(), input_id))
            connection.commit()
            return sql.execute('SELECT weight_up_to, output, weight_after FROM users WHERE tg_id=? AND datetime=?;', (tg_id, dt.date.today())).fetchall()


def checker2_db(tg_id, datetime, output='NULL'):
    user2 = sql.execute('SELECT datetime, input_id, weight_up_to, weight_after FROM users WHERE tg_id=?;', (tg_id,)).fetchall()
    if user2[-1][0] == str(dt.date.today()):
        sql.execute('UPDATE users SET output=? WHERE tg_id=? AND datetime=?;', (output, tg_id, dt.date.today()))
        connection.commit()
        return sql.execute('SELECT weight_up_to, output, weight_after FROM users WHERE tg_id=? AND datetime=?;', (tg_id, dt.date.today())).fetchall()


def add_weight_up_to_db(tg_id: int, weight_up_to: float, datetime):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user1 = sql.execute('SELECT datetime, input_id FROM users WHERE tg_id=?;', (tg_id, )).fetchall()
    if user1:
        input_id = user1[-1][-1]
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


def add_weight_after_db(tg_id: int, weight_after: float, datetime):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user1 = sql.execute('SELECT datetime, input_id FROM users WHERE tg_id=?;', (tg_id,)).fetchall()
    if user1:
        input_id = user1[-1][-1]
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
