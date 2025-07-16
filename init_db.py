import sqlite3

conn = sqlite3.connect("placementhub.db")
cursor = conn.cursor()

# Create the 'questions' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    solution_py TEXT,
    solution_java TEXT,
    category TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("✅ Table created successfully.")
