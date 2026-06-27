import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_file = os.path.join(BASE_DIR, "csv_files", "interns.csv")

with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)
def add_record(intern_id, name, email, domain):

    with open(csv_file, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            intern_id,
            name,
            email,
            domain
        ])

add_record(1, "Manju", "manju@gmail.com", "Web Development")
def search_record(name):

    with open(csv_file, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 1 and row[1] == name:
                print(row)

search_record("Manju")
def delete_record(name):

    rows = []

    with open(csv_file, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 1 and row[1] != name:
                rows.append(row)

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

delete_record("Manju")