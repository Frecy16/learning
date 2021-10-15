import sqlite3

conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute('create table user(id int primary key, name varchar(32))')
cursor.close()
conn.close()
