import sqlite3
from datetime import date

db = sqlite3.connect("engine/bot/Logs.db", check_same_thread=False)
c = db.cursor()


def writer(time, message):
    print(time, message)
    c.execute(f"""INSERT INTO Logs VALUES ('{time}', '{date.today()}', '{message}')""")
    db.commit()


def close_db():
    db.close()
