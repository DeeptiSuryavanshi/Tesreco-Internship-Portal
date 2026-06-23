def certificate_generator(names):
    for name in names:
        yield f"Certificate Generated for {name}"


students = ["Khushi", "Raushan"]

for c in certificate_generator(students):
    print(c)