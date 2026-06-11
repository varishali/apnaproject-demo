import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("INSERT INTO students VALUES (1,'Varish',85)")
cursor.execute("INSERT INTO students VALUES (2,'Ali',90)")

conn.commit()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()