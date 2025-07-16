from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")

# ---------------- CATEGORY PAGES ----------------
@app.route("/category/<category>")
def category_page(category):
    conn = sqlite3.connect('placementhub.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, solution_py, solution_java FROM questions WHERE category = ?", (category,))
    questions = cursor.fetchall()
    conn.close()
    return render_template("index.html", questions=questions, category=category)

# ---------------- ADMIN PAGE ----------------
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        question = request.form["question"]
        category = request.form["category"]
        solution = request.form["solution"]

        # Decide which fields to populate based on category
        if category == "dsa":
            solution_py = request.form["solution_py"]
            solution_java = request.form["solution_java"]
        else:
            # Non-code categories store everything in solution_py
            solution_py = solution
            solution_java = ""

        conn = sqlite3.connect('placementhub.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO questions (question, solution_py, solution_java, category) VALUES (?, ?, ?, ?)",
            (question, solution_py, solution_java, category)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("category_page", category=category))

    return render_template("admin.html")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app.run(debug=True)
