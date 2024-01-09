import requests
import re
from html import unescape

countries_with_densities = {}


def crawl_wikipedia(url):
    """
    Crawl a Wikipedia page and save its HTML content to a file.

    This function sends a GET request to the specified URL, retrieves the HTML content,
    and saves it to a file named 'crawling/density.txt' using UTF-16 encoding.

    :param url: The URL of the Wikipedia page to crawl.

    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/density.txt'
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
    """
    Extract the name of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the country name.

    :param string: The HTML string to search for the country name.

    :return: The extracted country name.
    """
    pattern = r'<a\s[^>]*?title="[^"]*"[^>]*>(.*?)</a>'

    match = re.search(pattern, string)

    if match:
        country_name = unescape(match.group(1))
        return country_name
    else:
        return "Country name not found."


def get_density_per_kilometer(string):
    """
    Extract the density of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the density of the country.

    :param string: The HTML string to search for the density of the country.

    :return: The extracted density of the country.
    """
    pattern = r'<td[^>]*?data-sort-value="([^"]*)"[^>]*>([^<]+)\n\s*'

    match = re.search(pattern, string)

    if match:
        number = match.group(2)
        return number
    else:
        return "Number not found."


def get_densities():
    """
    Parse and search for all the densities of the countries in the url from Wikipedia.

    :return: A dictionary containing the density of each country.
    """
    file_path = 'crawling/density.txt'
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
    # print(countries_with_densities)
    file.close()
    return countries_with_densities

# get_densities()
