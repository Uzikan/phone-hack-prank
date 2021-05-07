from random import *

guess=""

password=input("password")

letters = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]

while(guess != password):
    Guess=""
    for letter in password:
        guessletter=letters[randint(0,25)]
        guess=str(guessletter) + str(guess)
    print(guess)
input("")