age = int(input("Enter Your Age:"))
if age < 13 or age > 60:
    print("You are eligible for a discount on movie tickets.")
elif age >= 13 and age <= 60:    
    print("You are not eligible for a discount on movie tickets.")