import random
secret_number = random.randint(1, 100)
attempts = 0
print("Welcome to the Guessing Game! I have selected a number between 1 and 100.")

while (True):
    num = int(input("Enter your guess: "))
    attempts += 1

    if (num == secret_number):
        print("Congratulations! You guessed the number", num, "in", attempts, "attempts!")
    elif (num > secret_number and 0 < num < 101):
        print("Too High! Guess lower.\n")
    elif (num < secret_number and 0 < num < 101):
        print("Too Low! Guess higher.\n")
    else:
        print("Number Guessed is out of range! Try Again.\n")