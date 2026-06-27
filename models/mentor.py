class Mentor:
    def __init__(self, mentor_id, name, specialization):
        self.mentor_id = mentor_id
        self.name = name
        self.specialization = specialization

    def get_mentor_id(self):
        return self.mentor_id

    def get_name(self):
        return self.name

    def get_specialization(self):
        return self.specialization

    def set_name(self, name):
        self.name = name

    def set_specialization(self, specialization):
        self.specialization = specialization

    def __str__(self):
        return (
            f"Mentor ID: {self.mentor_id}, "
            f"Name: {self.name}, "
            f"Specialization: {self.specialization}"
        )
if __name__ == "__main__":
    mentor1 = Mentor(
        1,
        "Rahul Sharma",
        "Python Development"
    )
    mentor2 = Mentor(2, "Priya Singh", "App Development")
    mentor3 = Mentor(3, "Amit Verma", "Data Science")
    mentor4 = Mentor(4, "Neha Gupta", "Machine Learning")
    mentor5 = Mentor(5, "Karan Patel", "UI/UX Design")
    mentor6 = Mentor(6, "Anjali Mehta", "Cloud Computing")
    mentor7 = Mentor(7, "Rohit Kumar", "Cybersecurity")

    print(mentor1)
    print(mentor2)
    print(mentor3)
    print(mentor4)
    print(mentor5)
    print(mentor6)
    print(mentor7)