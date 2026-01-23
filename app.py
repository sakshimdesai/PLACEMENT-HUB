from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "placementhub.db"

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- CATEGORY PAGES ----------------
@app.route("/category/<category>")
def category_page(category):
    conn = sqlite3.connect("placementhub.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            question,
            solution,
            solution_py,
            solution_java
        FROM questions
        WHERE category = ?
    """, (category,))

    questions = cursor.fetchall()
    conn.close()

    return render_template(
        "index.html",
        questions=questions,
        category=category
    )

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

