import csv
import sqlite3

with open('roster.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

conn = sqlite3.connect('keyclub.sqlite')
c = conn.cursor()

c.executemany('INSERT INTO students VALUES(?,?,?,?)', data)

conn.commmit()
conn.close()
