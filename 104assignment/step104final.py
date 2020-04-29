#SQL Import and Creation of Database
import sqlite3
conn = sqlite3.connect('table.db')


cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS file
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)''')


#create table and column.
cur.execute("INSERT INTO  file(name) VALUES ('information.docx')")
cur.execute("INSERT INTO  file(name) VALUES ('Hello.txt')")
cur.execute("INSERT INTO  file(name) VALUES ('myImage.png')")
cur.execute("INSERT INTO  file(name) VALUES ('myMovie.mpg')")
cur.execute("INSERT INTO  file(name) VALUES ('World.txt')")
cur.execute("INSERT INTO  file(name) VALUES ('data.pdf')")
cur.execute("INSERT INTO  file(name) VALUES ('myPhoto.jpg')")
conn.commit()

row = ""

while conn:
    cur = conn.cursor()
    cur.execute("SELECT name FROM table WHERE name LIKE '%.txt' ")
    varSelectedFile = cur.fetchall()
    print(varSelectedFile)
conn.close()


    


