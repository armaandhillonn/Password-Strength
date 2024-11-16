"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Armaan Dhillon
Student ID: adhil28
File created: October 13, 2024
******************************
This file contains two functions: the first returns the number of character groups (lowercase, uppercase, digits,
symbols). The second evaluates password strength based on its length and character group variety, then returns the
strength.
"""

#intializes a function called count_groups
def count_groups(pwd):

#defines limits so character_groups doesnt get written twice
    character_groups = 0
    limit_for_lower = 0
    limit_for_upper = 0
    limit_for_digits = 0
    limit_for_symbols = 0

#intialize constants
    LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "1234567890"
    SYMBOLS = "!@#$%^&*/?-+=,.|~"

#for loop which runs until the length of the password
    for i in range(len(pwd)):
        char = pwd[i]

        #checks for any lowercase alphabet letter
        if limit_for_lower == 0 and char in LOWER_ALPHABET:
                character_groups += 1
                limit_for_lower += 1

        # checks for any uppercase alphabet letter
        if limit_for_upper == 0 and char in UPPER_ALPHABET:
                character_groups += 1
                limit_for_upper += 1

        # checks for any digits in password
        if limit_for_digits == 0 and char in DIGITS:
                character_groups += 1
                limit_for_digits += 1
        #checks for any symbols in password
        if limit_for_symbols == 0 and char in SYMBOLS:
                character_groups += 1
                limit_for_symbols += 1
    return character_groups

#intialized a function which returns the password's strength
def password_strength(pwd):

    password_length = len(pwd)
    total_groups = count_groups(pwd)
    pass_strength = 0

    # checks for /t, /n, or " " for every index in the password
    for char in ["\t", "\n", " "]:
        if char in pwd:
            return pass_strength
    # logic statements to determine password strength using the length of the password and the total groups
    if password_length < 5:
        pass_strength = 0
    elif 5 <= password_length <= 8:
        if 0 <= total_groups <= 1 :
            pass_strength = 1
        elif 2 <= total_groups <= 3 :
            pass_strength = 2
        elif total_groups == 4:
            pass_strength = 3
    elif 9 <= password_length <= 12:
        if 0 <= total_groups <= 1:
            pass_strength = 2
        elif 2 <= total_groups <= 3:
            pass_strength = 3
        elif total_groups == 4:
            pass_strength = 4
    elif password_length > 12:
        if 0 <= total_groups <= 1:
            pass_strength = 3
        elif 2 <= total_groups <= 3:
            pass_strength = 4
        elif total_groups == 4:
            pass_strength = 5
    return pass_strength







