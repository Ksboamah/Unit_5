# By Kwame Sakyi Boamah on Tuesday, October 22nd, 2019

import random

play = input("Do you want to play Guess it! (Yes)/(No)")
if play == "No":
    print("Thanks for playing. See you soon.")

number = random.randint(1, 101)
x = 0
number_of_guesses = 0
while x != number:
    x = int(input("What number did the computer pick?"))
    number_of_guesses += 1
    if x == number:
        print("You Guessed it")
    elif x < number:
        print("Your guess is too low.")
    else:
        x > number
        print("Your guess is too high.")
print("It took you", number_of_guesses, "tries.")
