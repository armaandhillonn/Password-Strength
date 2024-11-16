"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Armaan Dhillon
Student ID: adhil28
File created: October 13, 2024
******************************
This file generates and returns a password for the user by randomizing characters from a string constant
using the random library.
"""

import random

# function to generate a random password if the user chooses to
def generate_password(length):

    #constant with all legal possible characters
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"
    password = ""

    # for loop which appends many random character from ALL_CHARS into password.
    for i in range(length):
        random_letter = random.choice(ALL_CHARS)
        password += random_letter
    return password
