'''def greet(name):
    print("Hello", name)
for i in range(3):
    greet("Pratik")
    greet("Vidhi")
    greet("Aachal")'''


'''name = input("Enter your name: ")
age = int(input("Enter your age: "))
def greet(name , age):
    print("Hello", name, "You are", age, "years old.")
greet(name, age)'''


'''def multiply(a, b):
    return a * b
result = multiply(5, 4)
print("The result of 5 * 4 is:", result)
print("If you multiply more 10 in 5 * 4, you get:", result * 10)'''


'''def multiply(a, b):
    return a * b
result = multiply(int(input("Enter first number: ")), int(input("Enter second number: ")))
print("The result of multiplication is:", result)
result2 = multiply(result, int(input("Enter a number to multiply with the result:")))
print("The result of multiplication with the previous result is:", result2)'''


'''def multiply(a, b):
    return a * b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = multiply(num1, num2)
print("The result of multiplication, ", num1, " x ", num2, " is:", result)
num3 = int(input("Enter a number to multiply with the previous result " + str(result) + ": "))
result2 = multiply(result, num3)
print("The result of multiplication with, ", num1, " x ", num2, " x ", num3, " is:", result2)
print("The final result of multiplication is:", result2)'''

'''def welcome(name = "User"):
    if name == "":
        print("Welcome User to the world of Python programming!")
    else:
     print("Welcome", name, "to the world of Python programming!")
name = input("Enter your name: ")
welcome(name)'''


def calculate_total(a, b):
    return a + b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = calculate_total(num1, num2)
print("The result of addition, ", num1, " + ", num2, " is:", result)
num3 = int(input("Enter a number to add with the previous result " + str(result) + ": "))
result2 = calculate_total(result, num3)
print("The result of addition with, ", num1, " + ", num2, " + ", num3, " is:", result2)
print("The final result of addition is:", result2)
    