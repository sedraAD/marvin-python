#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

import marvin1
import marvin2
import inventory
import emission_functions

def main():
    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    marvin_image = r"""
                _,;;.,_
        ,-;;,_  ;,',,,'''@
    ,;;``  `'\\|//``-:;,.
    @`         ;^^^;      `'@
            :@ @:
            \ u /
    ,=,------)^^^(------,=,
    '-'-----/=====\-----'-'
            \_____/
        '`\ /_____\
        `\ \\_____/_
            \//_____\/|
            |        ||
            |        |'
            :________:`
    """

    bag = []
    stop = False
    while not stop:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        print("Hi, I'm Marvin. I know it all. What can I do you for?")
        print("1) Present yourself to Marvin.")
        print("2) Celsius to Farenheit.")
        print("3) Points to grades.")
        print("4) Calculate sum and average.")
        print("5) Repeat letters in word.")
        print("6) Is smaller, larger or equal.")
        print("7) Validate personnummer.")
        print("8) The Robber language.")
        print("9) Create personnummer.")
        print("10) Acronym creator.")
        print("11) Randomize letters.")
        print("12) Find indexes.")
        print("13) Search country.")
        print("14) Calculate change in emission.")
        print("15) Get a country data.")
        print("q) Quit.")
        print("\n\nTry out my 'inv' commands!")

        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "1":
            marvin1.greet()

        elif choice == "2":
            marvin1.celsius_to_fahrenheit()

        elif choice == "3":
            marvin1.points_to_grade()

        elif choice == "4":
            marvin1.sum_and_average()

        elif choice == "5":
            marvin1.hyphen_string()

        elif choice == "6":
            marvin1.compare_numbers()

        elif choice == "7":
            marvin1.validate_ssn()

        elif choice == "8":
            marvin1.robber_language()

        elif choice == "9":
            birthdate1 = input("Enter birthdate in (YYMMDD) format: ")
            print(marvin2.create_ssn(birthdate1))

        elif choice == "10":
            string1 = input("Enter something to create an acronym: ")
            print(marvin2.get_acronym(string1))

        elif choice == "11":
            original_string = input("Please enter a word or a phrase: ")
            randomized_string = marvin2.randomize_string(original_string)
            print(f"{original_string} --> {randomized_string}")

        elif choice == "12":
            main_string = input("Enter main string: ")
            sub_string = input ("Enter substring to find: ")
            print(marvin2.find_all_indexes(main_string, sub_string))

        elif choice == "13":
            country = input("Enter country name: ")
            try:
                result = emission_functions.search_country(country)
                print(f"Following countries were found: {result}")
            except ValueError as error:
                print(error)

        elif choice == "14":
            data = input("Please enter name of country and two years separated by a comma ex:(Sweden,2005,2017): ")
            try:
                country, year1, year2 = data.split(",")
                year1_int = int(year1)
                year2_int = int(year2)
                change = emission_functions.get_country_change_for_years(country, year1_int, year2_int)
                print(f"{country}:{change}%")
            except ValueError as error:
                print(error)

        elif choice == "15":
            country = input("Enter country name: ")
            country_data = emission_functions.get_country_data(country)
            emission_functions.print_country_data(country_data)

        elif "inv pick" in choice:
            parts = choice.split(" ")
            item = parts[2]
            if len(parts) > 3:
                position = parts[3]
                print(inventory.pick(bag, item, position))
            else:
                print(inventory.pick(bag, item))


        elif choice == "inv":
            print(inventory.inventory(bag))

        elif "inv drop" in choice:
            parts = choice.split(" ")
            item = parts[2]
            print(inventory.drop(bag, item))

        elif "inv swap" in choice:
            parts = choice.split(" ")
            item1 = parts[2]
            item2 = parts[3]
            print(inventory.swap(bag, item1, item2))

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
