import countries_links
import unite_data
from crawling import capital_city
from crawling import area
from crawling import density
from crawling import government
from crawling import language
from crawling import time_zone
from crawling import neighbours
from crawling import population

all_countries = []
error = []

countries = countries_links.get_countries_links()
capital_cities = capital_city.get_capital_cities()
areas = area.get_areas()
densities = density.get_densities()
governments = government.get_governments()
languages = language.get_languages()
time_zones = time_zone.get_time_zones()
neighbour = neighbours.get_neighbours_in_dict()
populations = population.get_population()
for i in range(len(countries)):
    if '_' in countries[i]:
        country = countries[i].replace('_', ' ')
    else:
        country = countries[i]
    if country == 'Danish Realm':
        country = 'Denmark'
    try:
        for key, value in capital_cities.items():
            if key == country or key in country:
                capital_city = capital_cities[key]
        for key, value in areas.items():
            if key == country or key in country:
                area = areas[key]
        for key, value in densities.items():
            if key == country or key in country:
                density = densities[key]
        for key, value in governments.items():
            if key == country or key in country:
                government = governments[key]
        for key, value in languages.items():
            if key == country or key in country:
                language = languages[key]
        for key, value in time_zones.items():
            if key == country or key in country:
                time_zone = time_zones[key]
        for key, value in neighbour.items():
            if key == country or key in country:
                actual_neighbour = neighbour[key]
        for key, value in populations.items():
            if key == country or key in country:
                population = populations[key]
        # print(country, capital_city, area, density)
        # print(government, language, time_zone, actual_neighbour, population)
        # print()
        country_data = unite_data.unite_data_about_country(country, capital_city, area, density, government,
                                                           language, time_zone, actual_neighbour, population)
        all_countries.append(country_data)
    except:
        error.append(country)
        print('Some error occurred at: ' + country)
# print("Errors: " + str(error))
# print(all_countries)

