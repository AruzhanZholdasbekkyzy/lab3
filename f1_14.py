import random

# Guess the number game
def guess_the_number():
    print("I'm thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    while int(input("Take a guess: ")) != number:
        print("Try again!")
    print("You got it!")

guess_the_number()