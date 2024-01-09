import requests

country_data = {
    'country_name': '',
    'capital_city': '',
    'population': '',
    'density': '',
    'area': '',
    'neighbours': '',
    'language': '',
    'time_zone': '',
    'government': ''
}


def initialize_country_data():
    global country_data
    country_data = {
        'country_name': '',
        'capital_city': '',
        'population': '',
        'density': '',
        'area': '',
        'neighbours': '',
        'language': '',
        'time_zone': '',
        'government': ''
    }


def unite_data_about_country(country, capital_city, area, density, government, language, time_zone, neighbour, population):
    """
    Create a dictionary with information about a country.

    This function initializes a dictionary containing various details about a country,
    such as its name, capital city, population, population density, area, neighbors,
    language, time zone, and type of government.

    :param country: The name of the country.
    :param capital_city: The capital city of the country.
    :param area: The area of the country.
    :param density: The density of the country.
    :param government: The type of government in the country.
    :param language: The official language spoken in the country.
    :param time_zone: The time zone of the country.
    :param neighbour: A list of neighboring countries.
    :param population: The population of the country.

    :return: A dictionary containing information about the specified country.
    """
    initialize_country_data()
    #######################################################################
    country_data['country_name'] = country
    country_data['capital_city'] = capital_city
    country_data['population'] = population
    country_data['density'] = density
    country_data['area'] = area
    country_data['neighbours'] = neighbour
    country_data['language'] = language
    country_data['time_zone'] = time_zone
    country_data['government'] = government
    #######################################################################
    return country_data
