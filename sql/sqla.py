import sqlite3


conn = sqlite3.connect("new.db")


cursor = conn.cursor()

cursor.execute('''ALTER TABLE population 
                  ADD zip INT;''')

conn.close()