# By Kwame Sakyi Boamah on Tuesday, October 22nd, 2019

import random

play = input("Do you want to play Guess it! (Yes)/(No)")
if play == "No":
    print("Thanks for playing. See you soon.")

number = random.randint(1, 101)

x = int(input("What number did the computer pick?"))
if x == number:
    print("You Guessed it in")
elif x < number:
    print("Your guess is too low.")
    x
else:
    x > number
    print("Your guess is too high.")
    x
    