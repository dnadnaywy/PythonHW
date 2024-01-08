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
