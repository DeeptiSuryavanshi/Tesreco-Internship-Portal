import copy

projects = ["Portal", "Attendance"]

shallow = copy.copy(projects)
deep = copy.deepcopy(projects)

projects.append("Performance")

print("Original:", projects)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)