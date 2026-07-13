import random
secret_number = random.randint(1, 100)
attempts = 1
guess = int(input("Guess the secret number between 1 and 100:"))

while guess != secret_number:
    attempts = attempts + 1
    if guess < secret_number:
        print("Too low! Try again.")
        
    else:
        print("Too high! Try again.")   
    guess = int(input("Guess the secret number between 1 and 100:"))
print("Congratulations! You guessed the secret number:", secret_number)
print("You guessed it in", attempts, "attempts.")
