import sqlite3

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute(
    "INSERT INTO students VALUES(1,'Varish',90)"
)

conn.commit()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()

print(data)

conn.close()
