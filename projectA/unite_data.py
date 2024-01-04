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


def unite_data_about_country(country, capital_cities, areas, densities, governments, languages, time_zones, neighbour, populations):
    initialize_country_data()
    #######################################################################
    country_data['country_name'] = country

    #######################################################################
    return country_data
