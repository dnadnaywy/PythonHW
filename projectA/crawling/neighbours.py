import requests
import re

neighbours = {}


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/neighbours.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders'
# crawl_wikipedia(wikipedia_url)

def print_dict(dict):
    for key, value in dict.items():
        print("Country: " + key + " has these neighbours: " + str(value))


def get_country_name(string):
    match = re.search(r'title="([^"]+)"', string)

    if match:
        country_name = match.group(1)
        return country_name
    else:
        return "Country name not found."


def get_neighbours(string):
    matches = re.findall(r'title="([^"]+)"', string)

    if matches:
        neighbours = matches
        return neighbours
    else:
        return "no neighbours found."


def get_neighbours_in_dict():
    file_path = 'crawling/neighbours.txt'
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

    table = table[19:]
    table = table[:-49]
    for i in range(0, len(table), 13):
        country_name = get_country_name(table[i + 1])
        country_neighbours = get_neighbours(table[i + 11])
        neighbours[country_name] = country_neighbours

    # print_dict(neighbours)

    file.close()
    return neighbours


# get_neighbours_in_dict()
