# Update, delete and select operations

import sqlite3

conn = sqlite3.connect('stud.db')

print('The database Connection is complete ')

# conn.execute('update stud set id=18 where id=10;')
conn.execute('delete from stud where id = 13;')
conn.commit()
print('The records deleted are: ', conn.total_changes)

data = conn.execute('select id,name from stud;')

for i in data:
    print('The id is : ', i[0], '|Name is :', i[1])

print('The data is selected')
conn.close()
