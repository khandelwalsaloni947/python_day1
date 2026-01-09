import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 10.")

secret_number = random.randint(1, 20)

guess = 0

while guess != secret_number:
   # print("secret_number...... ",secret_number)
    guess_text = input("Type a guess (1-20): ")
    guess = int(guess_text)

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
