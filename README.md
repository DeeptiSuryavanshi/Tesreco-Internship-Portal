# TESRECO Intern Management Portal

## 📌 Project Overview
TESRECO Intern Management Portal is a Flask-based web application designed to manage interns, mentors, attendance, and performance records efficiently. The system demonstrates advanced Python concepts along with database integration and web development using Flask.

---

## 🚀 Features

### 🐍 Advanced Python Modules
- OOP-based Intern Class design
- Custom Exceptions (Email & Duration validation)
- Decorators for performance logging
- Custom Iterator for Intern ID generation (TES001 format)
- Generator for certificate generation
- Shallow vs Deep copy demonstration
- Multiple Inheritance with MRO
- Abstract classes for report generation
- Functional programming (map, filter, reduce)
- Multithreading for parallel tasks
- Multiprocessing for performance report generation
- Logging system (tesreco.log)

---

### 🗄️ Database (SQLite)
- Interns table (CRUD operations)
- Mentors table
- Attendance tracking
- Mentor assignment system

---

### 🌐 Flask Web Application

#### Pages
- `/` → Home Page (TESRECO Welcome Page)
- `/about` → Organization details

#### APIs
- `POST /register` → Register new intern
- `GET /interns` → View all interns
- `PUT /intern/<id>` → Update intern details
- `DELETE /intern/<id>` → Delete intern
- `POST /attendance` → Mark attendance
- `POST /assign-mentor` → Assign mentor to intern

---

## 🏗️ Project Structure
tesreco-intern-portal/
│
├── app.py
├── models.py
├── oop_classes.py
├── decorators.py
├── exceptions.py
├── iterators.py
├── generators.py
├── utils.py
│
├── database/
│ └── interns.db
│
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── add_intern.html
│ ├── view_interns.html
│
├── static/
│ └── style.css
│
├── logs/
│ └── tesreco.log
│
└── README.md

---

## ⚙️ Tech Stack
- Python 3
- Flask
- SQLite3
- HTML/CSS (Jinja2 Templates)
- Logging module
- Threading & Multiprocessing

---

## ▶️ How to Run

```bash
# Install dependencies
pip install flask

# Run application
python app.py
http://127.0.0.1:8000/