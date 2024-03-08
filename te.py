import random

secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Welcome to the Guessing Game! Try to guess the secret number between 1 and 10.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number}.")
        break
    else:
        print("Try again!")
        attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")






