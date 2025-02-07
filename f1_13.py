import random

def guess_the_number():
    print("Hello! What is your name?")
    name=input()

    number=random.randint(1, 20)
    print("Well,",name, ", I am thinking of a number between 1 and 20.")
    gueses = 0 
    while True:
        print("Take a guess.")
        a=int(input()) 
        gueses+=1
        if a<number:
            print("Your guess is too low.")
        elif a>number:
            print("Your guess is too high.")
        else:
            print("Good job,",name,"! You guessed my number in",gueses, "guesses!")
            break  
guess_the_number()