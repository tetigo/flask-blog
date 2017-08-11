import sqlite3

with sqlite3.connect('blog.db') as conn:
	cursor = conn.cursor()
	cursor.execute('create table posts (title text, post text)')
	cursor.execute('insert into posts values("Good", "I\'m good.")')
	cursor.execute('insert into posts values("Well","I\'m well.")')
	cursor.execute('insert into posts values("Okay","I\'m okay.")')


	