#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import random

def calculate_luhna_sum(number):
    """
    Calculates the Luhn sum for a given number.
    """
    total_sum = 0
    for i, digit in enumerate(number):
        num = int(digit)
        if i % 2 == 0:
            num *= 2
            if num > 9:
                num -= 9
        total_sum += num
    return total_sum


def create_ssn(birthdate):
    """
    Creates the 4 last digits in a Swedish personnummer.
    """
    random_int = ""
    for _ in range(3):
        random_int += str(random.randint(0,9))
    partial_personnummer = birthdate + random_int
    luhn_sum = calculate_luhna_sum(partial_personnummer)
    last_digit = (10 - (luhn_sum % 10)) % 10
    return birthdate + "-" + random_int + str(last_digit)


def get_acronym(string):
    """
    Extracts and returns the acronym of a given string.
    """
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += char
    return new_string


def randomize_string(input_string):
    """
    Randomizes the letters in a given string.
    """
    randomized_string = ""
    lenght = len(input_string)
    while lenght > 0:
        index = random.randint(0, lenght -1)
        randomized_string += input_string[index]
        input_string = input_string[:index] + input_string[index + 1:]
        lenght -= 1
    return randomized_string
    

def find_all_indexes(main, sub):
    """
    Finds all indexes of the sub_string in the main_string and returns them as a comma-separated string.
    """
    result = ""
    start = 0
    first = True
    while True:
        try:
            index = main.index(sub, start)
            if first:
                result += str(index)
                first = False
            else:
                result += "," + str(index)
            start = index + 1
        except ValueError:
            break
    return result
