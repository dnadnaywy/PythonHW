import requests
import re
from html import unescape

countries_with_densities = {}


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'density.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density'
# crawl_wikipedia(wikipedia_url)

def get_country(string):
    pattern = r'<a\s[^>]*?title="[^"]*"[^>]*>(.*?)</a>'

    match = re.search(pattern, string)

    if match:
        country_name = unescape(match.group(1))
        return country_name
    else:
        return "Country name not found."


def get_density_per_kilometer(string):
    pattern = r'<td[^>]*?data-sort-value="([^"]*)"[^>]*>([^<]+)\n\s*'

    match = re.search(pattern, string)

    if match:
        number = match.group(2)
        return number
    else:
        return "Number not found."


def get_densities():
    file_path = 'density.txt'
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

    table = table[27:]
    i = 0
    internal_counter = 1
    internal_row = []
    while i < len(table):
        if table[i] == "<tr>\n":
            country = get_country(internal_row[0])
            density = get_density_per_kilometer(internal_row[1])
            countries_with_densities[country] = density

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
        i += 1
    print(countries_with_densities)
    file.close()
    # return countries_with_link


get_densities()
