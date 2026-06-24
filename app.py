from flask import Flask, flash, url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import flask
from datetime import datetime
from database.db import get_connection
from utils.decorators import log_performance
from database.crud import *

import os
import sys
import importlib.util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

db_module_path = os.path.join(BASE_DIR, "database", "create_tables.py")
spec = importlib.util.spec_from_file_location("database.create_tables", db_module_path)
db_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(db_module)

get_connection = db_module.get_connection
create_tables = db_module.create_tables

app = Flask(__name__)
app.secret_key = "tesreco-dev-secret"


# Temporary data storage
interns = ["id"]

next_id = 1


create_tables()

DOMAINS = [
    "Web Development", "App Development", "Data Science",
    "Machine Learning", "UI/UX Design", "Cloud Computing", "Cybersecurity",
]


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


# home page and about page

@app.route("/")
def home():
    return render_template("home.html", active_page="home")
#about page
@app.route("/about")
def about():
    return render_template("about.html", active_page="about")
# add kar rhe h intern and mentor ka data
@app.route("/add-intern", methods=["GET", "POST"])
def add_intern():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        domain = request.form.get("domain", "").strip()

        if name and email and domain:
            conn = get_connection()
            conn.execute(
                "INSERT INTO interns (name, email, domain) VALUES (?, ?, ?)",
                (name, email, domain),
            )
            conn.commit()
            conn.close()
            flash(f"{name} was added successfully.")
            return redirect(url_for("view_interns"))
        else:
            flash("Please fill in all fields.")

    return render_template("add_intern.html", active_page="add", domains=DOMAINS)
@app.route("/view-interns")
def view_interns():

    conn = get_connection()

    interns = conn.execute("SELECT * FROM interns ORDER BY intern_id").fetchall()
    conn.close()
    return render_template("view_interns.html", active_page="view", interns=interns)

# edit and delete intern data
@app.route("/edit-intern/<int:intern_id>", methods=["GET", "POST"])
def edit_intern(intern_id):
    conn = get_connection()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        domain = request.form.get("domain", "").strip()

        if name and email and domain:
            conn.execute(
                "UPDATE interns SET name = ?, email = ?, domain = ? WHERE intern_id = ?",
                (name, email, domain, intern_id),
            )
            conn.commit()
            conn.close()
            flash(f"{name}'s details were updated successfully.")
            return redirect(url_for("view_interns"))
        else:
            flash("Please fill in all fields.")

    intern = conn.execute(
        "SELECT * FROM interns WHERE intern_id = ?", (intern_id,)
    ).fetchone()
    conn.close()

    if intern is None:
        flash("That intern no longer exists.")
        return redirect(url_for("view_interns"))

    return render_template(
        "edit_intern.html", active_page="view", intern=intern, domains=DOMAINS
    )
@app.route("/delete-intern/<int:intern_id>", methods=["POST"])
def delete_intern(intern_id):
    conn = get_connection()
    conn.execute("DELETE FROM interns WHERE intern_id = ?", (intern_id,))
    conn.commit()
    conn.close()
    flash("Intern was deleted successfully.")
    return redirect(url_for("view_interns"))

@app.route("/add-mentor", methods=["GET", "POST"])
def add_mentor():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        specialization = request.form.get("specialization", "").strip()

        if name and specialization:
            conn = get_connection()
            conn.execute(
                "INSERT INTO mentors (name, specialization) VALUES (?, ?)",
                (name, specialization),
            )
            conn.commit()
            conn.close()
            flash(f"{name} was added as a mentor.")
            return redirect(url_for("view_mentors"))
        else:
            flash("Please fill in all fields.")
            
    return render_template("add_mentor.html", active_page="add_mentor")


@app.route("/view-mentors")
def view_mentors():
    conn = get_connection()
    mentors = conn.execute("SELECT * FROM mentors ORDER BY mentor_id").fetchall()
    conn.close()
    return render_template("view_mentors.html", active_page="view_mentors", mentors=mentors)

@app.route("/attendance")
def attendance_page():

    conn = get_connection()

    interns = conn.execute(
        "SELECT * FROM interns"
    ).fetchall()

    attendance_logs = conn.execute("""
        SELECT attendance.date,
               interns.name,
               attendance.status
        FROM attendance
        JOIN interns
        ON attendance.intern_id = interns.intern_id
        ORDER BY attendance.id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "attendance.html",
        interns=interns,
        attendance_logs=attendance_logs,
        active_page="attendance"
    )
@app.route("/mark-attendance", methods=["POST"])
def mark_attendance():

    intern_id = request.form["intern_id"]
    date = request.form["date"]
    status = request.form["status"]

    conn = get_connection()

    conn.execute(
        "INSERT INTO attendance (intern_id, date, status) VALUES (?, ?, ?)",
        (intern_id, date, status)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("attendance_page"))
if __name__ == "__main__":
    app.run(debug=True, port=8000)