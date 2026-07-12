username = input("Enter your username: ")
password = input("Enter your password: ")

balance = 5000

if username == "Pratik" and password == "python123":
    print("Welcome to the ATM")

    balance_check = input("Do you want to check your balance? (yes/no): ")

    if balance_check.lower() == "yes":
        print("Your current balance is:", balance)
    else:
        print("Thank you for visiting.")

else:
    print("Invalid username or password. Please try again.")