students = {} #empty dictionary
students[1] = "Bakari"
print(students[1])
students[2] = "Ibrahim"
print(students)

for key in students:
    print(students[key])

print(1 in students)
print(tuple(students.items()))
del students[1]
print(students)
print(len(students))
