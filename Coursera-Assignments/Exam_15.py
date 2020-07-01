import sqlite3

conn=sqlite3.connect('test.sqlite')
cur=conn.cursor()

cur.execute("""drop table Ages""")
cur.execute("""CREATE TABLE Ages (name VARCHAR(128), age INTEGER)""")

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Thorben', 21))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Clare', 24))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Joynul', 36))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Safara', 21))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Kames', 28))

conn.commit()
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur.fetchone():
    print(row)
    
