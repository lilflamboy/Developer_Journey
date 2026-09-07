'''students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
user_name = input("Enter the name of the student to search: ")
found = False
for student in students:
    if student["name"] == user_name:
        print("Student found!")
        print(student["name"] + " is " + str(student["age"]) + " years old.")
        found = True
if not found:
    print("Student not found!")'''

'''students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
input_name = input("Enter the name of the student to update: ")
input_age = int(input("Enter the new age of the student: "))
found = False
for student in students:
    if student["name"] == input_name:
        student["age"] = input_age
        print("Student age updated successfully!")
        found = True
if not found:
    print("Student not found!")
print(students)'''

'''students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
remove_name = input("Enter the name of the student to remove: ")
found = False
for student in students:
    if student["name"] == remove_name:
        students.remove(student)
        print("Student removed successfully!")
        found = True
if not found:
    print("Student not found!")
print(students)'''

students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
input_name = input("Enter the name of the student to update: ")
found = False
for student in students:
    if student["name"] == input_name:
        print("name", student["name"])
        print("age", student["age"])
        input_age = int(input("Enter the new age of the student: "))
        student["age"] = input_age
        print("Student age updated successfully!")
        found = True
if not found:
    print("Student not found!")
print(students)