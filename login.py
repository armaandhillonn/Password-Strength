"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Armaan Dhillon
Student ID: adhil28
File created: October 13, 2024
******************************
This file uses functions to create a login screen. It prompts the user to enter a password,
checks its strength, and offers an option to generate a random password.
"""

from password import *
from generate import *

#Intializes a function which creates the usr interface and uses all previous functions.
def process_password(min_strength):
    keep_running = True

    #while loop which keeps running until a strong enough password is created.
    while keep_running:
        user_input_pass = (input("Type in a new password or type X for a randomly generated password: "))

        #logic for a randomly generated password
        if user_input_pass == "x" or user_input_pass == "X":
            generated_pass = generate_password(15)
            print("Your password: " + generated_pass)
            print("Your password has a strength of " , password_strength(generated_pass))
            print("Your password is strong enough! Thank you.")
            keep_running = False

        #logic for a user entered password
        else:
            print("You entered: " + user_input_pass)
            print("Your password has a strength of ", password_strength(user_input_pass))
            if password_strength(user_input_pass) >= min_strength:
                print("Your password is strong enough! Thank you.")
                keep_running = False
            else:
                print("Your password is not strong enough. Please create a new password that is stronger.\n")
