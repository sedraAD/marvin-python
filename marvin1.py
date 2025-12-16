#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin2

def greet():
    """
    Asks the user to enter their name and prints a greeting for them.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hi {name} - great to see you!")
    print("How can I help you today?")


def celsius_to_fahrenheit():
    """
    Converts a temperature from Celsius to Farenheit.
    """
    celsius = float(input("Enter temperature in °C, and press enter: "))
    farenheit = (celsius*9)/5 + 32
    print (f"\n{celsius} °C is equivalent to {round(farenheit, 2)} °F.")


def points_to_grade():
    """
    Converts points to grade based by precentage.
    """
    maximum_points = float(input("What is the maximum possible points? "))
    user_points = float(input("What is your points? "))
    percentage = (user_points/maximum_points)*100
    if percentage >= 90:
        print("\nscore: A")
    elif 80 <= percentage < 90:
        print("\nscore: B")
    elif 70 <= percentage < 80:
        print("\nscore: C")
    elif 60 <= percentage < 70:
        print("\nscore: D")
    else:
        print("\nscore: F")


def sum_and_average():
    """
    Calculates sum and average of a series of numbers.
    """
    numbers = 0
    count = 0
    while True:
        user_input = input("Enter number (or type 'done' to finsih): ")
        if user_input.lower() == "done": 
            break
        try: 
            number = float(user_input)
            numbers += number
            count += 1
        except ValueError:
            print("Please follow the instructions!")
    if count > 0:
        average = numbers/count
        print(f"\nThe sum of all numbers are {round(numbers, 2)} and the average is {round(average, 2)}.") 
    else:
        print("No numbers were entered.")


def hyphen_string():
    """
    Creates a hyphen separated string with repeated charachters.
    """
    new_string = ""
    count = 0
    string = input("Type anything: ")
    for i, letter in enumerate(string):
        count += 1
        new_string += letter*count
        if i < len(string) - 1:
            new_string += "-"
    print(new_string)


def compare_numbers():
    """
    Compares a series of numbers entered by the user.
    """
    print("Welcome to Marvin's number comparison! \n")
    previous_number = None
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            if previous_number is None:
                previous_number = number
                print("Please enter another number to compare.")
            else :
                if number < previous_number:
                    print("smaller!")
                elif number > previous_number:
                    print("larger!")
                else:
                    print("same!")
                previous_number = number
        except ValueError:
            print("not a number!")


def validate_ssn():
    """
    Validates a Swedish personal number.
    """
    personnummer = input("Please Enter personnummer: ")
    clean_personnummer = ""
    for char in personnummer:
        if char.isdigit():
            clean_personnummer += char
    if len(clean_personnummer) != 10:
        print("Not valid")
    else:
        total_sum = marvin2.calculate_luhna_sum(clean_personnummer)
        if total_sum % 10 == 0:
            print("Valid")
        else:
            print("Not valid")


def robber_language():
    """
    Translates a word into the "Robebr language.
    """
    vowels = "a, e, i, o, u, y, å, ä, ö"
    new_word = ""
    word = input("Type any word: ")
    for letter in word.lower():
        if letter in vowels:
            new_word += letter
        else:
            new_letter = letter + "o" + letter
            new_word += new_letter
    print (new_word)
