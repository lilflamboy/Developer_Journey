students = ["Pratik", "Rahul", "Amit", "Sneha", "Riya"]
marks = [85, 42, 91, 67, 78]
passed_students = []
for i in range(len(students)):
    if marks[i] >= 75:
        passed_students.append(students[i])
print(passed_students)