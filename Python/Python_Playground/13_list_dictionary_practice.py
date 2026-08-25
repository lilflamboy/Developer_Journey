"""students = [
    {"name": "Pratik", "age": 20},
    {"name": "Rahul", "age": 22},
    {"name": "Amit", "age": 20}
]
students.append({"name": "Neha", "age": 21})
print(students)
students[2]["age"] = 21
for student in students:
    if student["age"] > 20:
        print(student["name"])"""

"""students = []
student = {}      
input_name = input("name: ")
student["name"] = input_name
input_age = input("age: ")
student["age"] = int(input_age)
students.append(student)
print(students)"""

students = []
for i in range(3):
    student = {}
    input_name = input("name: ")
    student["name"] = input_name
    input_age = input("age: ")
    student["age"] = int(input_age)
    students.append(student)
print(students)    
for student in students:
    if student["age"] > 20:
        print(student["name"] + " is older than rest of the students.")

