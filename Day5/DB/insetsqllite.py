# Insert operation
# import mysql connector

import sqlite3

conn = sqlite3.connect('stud.db')

print('The database Connection is complete ')

conn.execute('insert into stud values(11,"Shruti")')
conn.execute('insert into stud values(12,"Neha")')
conn.execute('insert into stud values(13,"Suresh")')
conn.execute('insert into stud values(14,"Rohan")')
print('The Data is inserted')

conn.commit()
conn.close()