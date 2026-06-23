from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Interns(
    intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    domain TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Mentors(
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS MentorAssignment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_id INTEGER,
    mentor_id INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intern_id INTEGER,
    date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Tables created successfully!")