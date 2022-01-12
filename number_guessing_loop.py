#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 11, 2022
# This program allows a user to guess a number between
# 0 and 9 when the initial number is randomly generated until
# they get it right

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():
    # This function asks for the users number and
    # then compares it to the constant

    # Randomly generate the number
    rand_num = random.randint(0, 9)

    # Display intro
    print(Fore.WHITE + "I have picked a number between 0 and 9.")
    time.sleep(1)
    print(Fore.WHITE + "Guess my number!!!")
    print(Fore.BLUE + " ")

    # Loop that asks user to enter guesses until they are right
    while True:

        user_num = (input("Enter your guess: "))
        try:
            # Make sure user input is an integer
            user_num_int = int(user_num)

            # Makes sure that user number is positive
            if user_num_int >= 0:
                # Evaluate acceptable integer
                time.sleep(1)
                print(Fore.CYAN + " ")
                if user_num_int == rand_num:
                    print("You guessed it! Most impressive.")
                    break
                else:
                    print(Fore.BLUE + "Sorry, that is incorrect. Try again")
                    print("")
                    time.sleep(1)

            else:
                print("{} is not a positive number.".format(user_num_int))

        except Exception:
            # Prevent crash by displaying error message if user
            # input is not an integer
            print(" ")
            print("'{}' is not a number".format(user_num))


if __name__ == "__main__":
    main()
