from html.parser import HTMLParser
import requests
import re


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'population.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
# crawl_wikipedia(wikipedia_url)

countries = {}


def get_country(string, contor):
    match = re.search(r'<a[^>]*>(.*?)</a>', string)

    if match:
        country_name = match.group(1)
        return country_name, contor
    else:
        contor += 1
        return "Country name not found.", contor


def get_population_number(string):
    match = re.search(r'<td style="text-align:right">([\d,]+)</td>', string)

    if match:
        population_number = match.group(1).replace(',', '')  # Remove commas
        return population_number
    else:
        return "Population not found."


def print_dict(dict):
    for key, value in dict.items():
        print("Country: " + key + " has " + value + " population")


def get_population():
    file_path = 'population.txt'
    file = open(file_path, 'r', encoding='utf-16')
    html_line = file.readline()
    table = []
    in_table = False
    while html_line:
        html_line = file.readline()
        if '<table class="wikitable sortable' in html_line:
            in_table = True
        if '</table' in html_line and in_table is True:
            in_table = False

        if in_table:
            table.append(html_line)

    table = table[26:]
    contor = 0
    for i in range(0, len(table), 13):
        country_name, contor = get_country(table[i + 3], contor)
        population = get_population_number(table[i + 5])
        countries[country_name] = population

    print_dict(countries)
    file.close()


get_population()
