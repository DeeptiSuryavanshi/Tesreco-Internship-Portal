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

from database.crud import get_all_interns, get_all_interns

app = Flask(__name__)
app.secret_key = "tesreco-dev-secret"


# Temporary data storage
interns = ["id"]

next_id = 1


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


# Home Page
@app.route("/")
def home():
    return render_template("home.html", active_page="home")


# About Page
@app.route("/about")
def about():
    return render_template("about.html", active_page="about")


# Add Intern
@app.route("/add-intern", methods=["GET", "POST"])
def add_intern_page():
    global next_id

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        domain = request.form.get("domain")
        
        conn = get_connection()

        conn.execute("""
        INSERT INTO Interns(name,email,domain)
        VALUES(?,?,?)
        """, (name, email, domain))

        conn.commit()
        conn.close()
        if name and email and domain:

            interns.append({
                "id": next_id,
                "name": name,
                "email": email,
                "domain": domain
            })

            next_id += 1

            flash("Intern added successfully!")

            return redirect(url_for("view_interns"))

        flash("Please fill all fields.")

    return render_template(
        "add_intern.html",
        active_page="add"
    )


# View Interns
@app.route("/view-interns")
def view_interns():

    conn = get_connection()

    interns = conn.execute(
        "SELECT * FROM Interns"
    ).fetchall()

    conn.close()

    return render_template(
        "view_interns.html",
        active_page="view",
        interns=interns
    )

@app.route("/attendance")
def attendance_page():

    conn = get_connection()

    interns = conn.execute(
        "SELECT * FROM Interns"
    ).fetchall()

    attendance_logs = conn.execute("""
        SELECT Attendance.date,
               Interns.name,
               Attendance.status
        FROM Attendance
        JOIN Interns
        ON Attendance.intern_id = Interns.intern_id
        ORDER BY Attendance.id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "attendance.html",
        interns=interns,
        attendance_logs=attendance_logs
    )
@app.route("/mark-attendance", methods=["POST"])
def mark_attendance():

    intern_id = request.form["intern_id"]
    date = request.form["date"]
    status = request.form["status"]

    conn = get_connection()

    conn.execute("""
    INSERT INTO Attendance
    (intern_id,date,status)
    VALUES(?,?,?)
    """,(intern_id,date,status))

    conn.commit()
    conn.close()

    return redirect("/attendance")

# Delete Intern
@app.route("/delete-intern/<int:intern_id>")
def delete_intern(intern_id):

    global interns

    interns = [
        intern
        for intern in interns
        if intern["id"] != intern_id
    ]

    flask.flash("Intern deleted successfully!")

    return redirect(url_for("view_interns"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)