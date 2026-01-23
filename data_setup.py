import json
import sqlite3

print("📢 Running FINAL data_setup.py")

# Load JSON data
with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect("placementhub.db")
cursor = conn.cursor()

inserted = 0

for item in data:
    try:
        question = item["question"]
        category = item["category"].strip().lower()

        # Default values
        solution = ""
        solution_py = ""
        solution_java = ""

        if category == "dsa":
            solution_py = item.get("solution_py", "")
            solution_java = item.get("solution_java", "")
        else:
            solution = item.get("solution", "")

        cursor.execute(
            """
            INSERT INTO questions (question, solution, solution_py, solution_java, category)
            VALUES (?, ?, ?, ?, ?)
            """,
            (question, solution, solution_py, solution_java, category)
        )

        inserted += 1

    except KeyError as e:
        print(f"⚠️ Skipped: {item.get('question', 'UNKNOWN')} - missing {e}")

conn.commit()
conn.close()

print(f"✅ Inserted {inserted} questions into the database.")
