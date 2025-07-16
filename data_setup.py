import json
import sqlite3

print("📢 Running FINAL data_setup.py")

# Connect to the SQLite database
conn = sqlite3.connect('placementhub.db')
cursor = conn.cursor()

# Load JSON data
with open('questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# If nested list (e.g. [[{}, {}, ...]]) flatten it
if isinstance(data, list) and len(data) == 1 and isinstance(data[0], list):
    data = data[0]

# Validate top-level data
if not isinstance(data, list):
    raise ValueError("❌ JSON must contain a list of questions.")

count = 0

# Insert into database
for q in data:
    try:
        if q['category'] == 'dsa':
            cursor.execute('''
                INSERT INTO questions (question, solution_py, solution_java, category)
                VALUES (?, ?, ?, ?)
            ''', (q['question'], q['solution_py'], q['solution_java'], q['category']))
        else:
            cursor.execute('''
                INSERT INTO questions (question, solution_py, solution_java, category)
                VALUES (?, ?, ?, ?)
            ''', (q['question'], q['solution'], '', q['category']))
        count += 1
    except Exception as e:
        print(f"⚠️ Skipped: {q.get('question', '[unknown]')} - {e}")

# Commit and close
conn.commit()
conn.close()

print(f"\n✅ Inserted {count} questions into the database.")
