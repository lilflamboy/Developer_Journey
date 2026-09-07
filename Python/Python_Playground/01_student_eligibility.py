'''name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome,", name, "you are eligible to vote.")
else:
    print("Welcome", name, "You are not eligible to vote.") 
       
print("Thank you for using our program.")'''    


'''age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:   
    print("You are a senior citizen.")'''


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name} is {age} years old and can vote.")
else:
    print(f"{name} is {age} years old and cannot vote yet.")