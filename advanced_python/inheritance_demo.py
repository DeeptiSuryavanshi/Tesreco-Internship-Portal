class Person:
    pass

class Employee:
    pass

class Mentor:
    pass

class TESRECOMentor(Person, Employee, Mentor):
    pass

print(TESRECOMentor.mro())