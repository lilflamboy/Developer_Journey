name = (input("Enter your name: "))
marks = int(input("Enter your marks: "))
print("Welcome", name)
if marks >= 90:
    print("You have scored an A grade.")
elif marks >= 75:
    print("You have scored a B grade.")
elif marks >= 35:
    print("You have pass the exam.")    
else:
    print("You have failed the exam.")    

print("Thank you for using grading system.") 