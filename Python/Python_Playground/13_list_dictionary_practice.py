students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
students.append({"name": "Neha", "age": 21})
print(students)
students[2]["age"] = 21
for student in students:
    if student["age"] > 20:
        print(student["name"])