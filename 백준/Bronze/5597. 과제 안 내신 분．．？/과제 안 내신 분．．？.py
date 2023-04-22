students = []
for i in range(28):
    students.append(int(input()))
# print(students)
for n in range(1, 31):
    if n not in students:
        print(n)