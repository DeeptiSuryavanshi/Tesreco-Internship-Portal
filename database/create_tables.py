from database.db import get_connection
import sqlite3
import os

conn = get_connection()
cur = conn.cursor()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "tesreco.db")


def get_connection():
    """Return a new SQLite connection with row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """Create the interns and mentors tables if they don't already exist."""
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS interns (
            intern_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT NOT NULL,
            email     TEXT NOT NULL,
            domain    TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS mentors (
            mentor_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name           TEXT NOT NULL,
            specialization TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intern_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL
       )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print(f"Tables verified/created in {DB_PATH}")