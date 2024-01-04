from time import sleep
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

if __name__ == '__main__':
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
        # try:
        capital_city = capital_cities[country]
        area = areas[country]
        density = densities[country]
        government = governments[country]
        language = languages[country]
        time_zone = time_zones[country]
        actual_neighbour = neighbour[country]
        population = populations[country]
        print(country, capital_city, area, density)
        print(government, language, time_zone, actual_neighbour, population)
        print()
        # country_data = unite_data.unite_data_about_country(country, capital_cities, areas, densities, governments, languages, time_zones, neighbours, populations)
        # all_countries.append(country_data)
        # print(country_data)
        # sleep(3)
    # except:
    #     error.append(country)
    #     print('Some error occurred at: ' + country)
    # print("Errors: " + str(error))
