import sqlite3
from os import path

conn = sqlite3.connect(path.join('..', 'db', 'metadata.db'))
c = conn.cursor()

c.execute('SELECT * FROM metadata')
print(c.fetchall())
