import sqlite3 as lite
import sys


con = lite.connect('coin.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT dollar FROM coins WHERE data LIKE '%2022%'")
    rows = cur.fetchall()

    for row in rows:
        print(row)
