# Connecting to database and creating table

# import mysql connector

import sqlite3

conn = sqlite3.connect('stud.db')

print('The database Connection is complete ')

conn.execute('''create table stud(id integer(4),name text(30));''')
print('The table is created')

conn.commit()
conn.close()