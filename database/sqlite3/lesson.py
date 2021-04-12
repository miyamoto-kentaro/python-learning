import sqlite3

'''
the basic way of creating database.
'''
# conn = sqlite3.connect('test_sqlite.db')

'''
use memory in private lessons.
:memory: keep updating, so we can try as many times as we like.
'''
conn = sqlite3.connect(':memory:')

'''
defanition a cursor at database
we manipulate the database by cursor
'''
curs = conn.cursor()

'''
CREATE method:
it create a table called persons.
we can prescribe fine settings.
'''
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

'''
INSERT method:
it insert object in a table.
'''
curs.execute(
    'INSERT INTO persons(name) values("MIKE")'
)
curs.execute(
    'INSERT INTO persons(name) values("Nancy")'
)
curs.execute(
    'INSERT INTO persons(name) values("Jun")'
)
conn.commit()

'''
APDATE method:
it edit the data.
this method APDATE change the persons, MIKE to mike.
'''
curs.execute('UPDATE persons set name = "Mike" WHERE name = "MIKE"')
conn.commit()

'''
DELETE method:
it delete the data.
this method delete mike from persons.
'''
curs.execute('DELETE FROM persons WHERE name = "Mike"')
conn.commit()

'''
SELECT method:
it search data in the table.
'''
curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.close()
conn.close()