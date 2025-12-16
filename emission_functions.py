#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

from emission_data import emission_1990, emission_2005, emission_2017, country_data

def search_country(search_word):
    """
    Search country data in country_data and return all countries that match.
    """
    search_word = search_word.lower()
    matches = (country for country in country_data if search_word in country.lower())
    matches = list(matches)
    if not matches:
        raise ValueError("Country does not exist!")
    return matches


def get_country_year_data_megaton(country, year):
    """
    Gets a countrys emission data in megaton a specific year.
    """
    country_id = country_data[country]["id"]
    emissions_data = {1990: emission_1990, 2005: emission_2005, 2017:emission_2017}
    if year not in emissions_data:
        raise ValueError("Wrong year!")
    emission = emissions_data[year][country_id]
    return emission*1000000


def get_country_change_for_years(country, year1, year2):
    """
    Calculates change in emission in a country between two given years.
    """
    emission_data = {}
    for year in [year1, year2]:
        emission_data[year] = get_country_year_data_megaton(country, year)
    change = ((emission_data[year2] - emission_data[year1])/emission_data[year1])*100
    return round(change, 2)


def get_country_data(country_name):
    """
    Get all country data.
    """
    years = [1990, 2005, 2017]
    emissions = {}
    populations = {}
    for year in years:
        emissions[year] = get_country_year_data_megaton(country_name, year)
        population_data = country_data.get(country_name, {}).get("population", [None, None, None])
        if len(population_data) > 0:
            year_index = years.index(year)
            populations[year] = population_data[year_index]
        else:
            populations[year] = None
    emission_change_1990_2005 = get_country_change_for_years(country_name, 1990, 2005)
    emission_change_2005_2017 = get_country_change_for_years(country_name, 2005, 2017)
    data = {
        'name' : country_name,
        1990: {'emission': emissions[1990], 'population': populations[1990]},
        2005: {'emission': emissions[2005], 'population': populations[2005]},
        2017: {'emission': emissions[2017], 'population': populations[2017]},
        'emission_change': (emission_change_1990_2005, emission_change_2005_2017)
    }
    return data


def print_country_data(data):
    """
    Prints country data.
    """
    country_name = data.get("name")
    print(country_name)
    years = [1990, 2005, 2017]
    for year in years:
        country_emission = data[year].get("emission")
        country_population = data[year].get("population")
        print(f"Emission - {year}: {country_emission}")
        if country_population is None:
            print("Missing population data!")
        else:
            print(f"Population - {year}: {country_population}")
    emission_change_1990_2005 = data.get('emission_change')[0]
    emission_change_2005_2017 = data.get('emission_change')[1]
    print(f"Emission change - 1990-2005: {emission_change_1990_2005}%   2005-2017: {emission_change_2005_2017}%")
