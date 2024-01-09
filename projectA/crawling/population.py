from html.parser import HTMLParser
import requests
import re


def crawl_wikipedia(url):
    """
    Crawl a Wikipedia page and save its HTML content to a file.

    This function sends a GET request to the specified URL, retrieves the HTML content,
    and saves it to a file named 'crawling/population.txt' using UTF-16 encoding.

    :param url: The URL of the Wikipedia page to crawl.

    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/population.txt'
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


def get_country(string):
    """
    Extract the name of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the country name.

    :param string: The HTML string to search for the country name.

    :return: The extracted country name.
    """
    match = re.search(r'<a[^>]*>(.*?)</a>', string)

    if match:
        country_name = match.group(1)
        return country_name
    else:
        return "Country name not found."


def get_population_number(string):
    """
    Extract the population of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the population of the country.

    :param string: The HTML string to search for the population of the country.

    :return: The extracted population of the country.
    """
    match = re.search(r'<td style="text-align:right">([\d,]+)</td>', string)

    if match:
        population_number = match.group(1).replace(',', '')  # Remove commas
        return population_number
    else:
        return "Population not found."


def get_population():
    """
    Parse and search for the population of the countries in the url from Wikipedia.

    :return: A dictionary containing the population of each country.
    """
    file_path = 'crawling/population.txt'
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
    for i in range(0, len(table), 13):
        country_name = get_country(table[i + 3])
        population = get_population_number(table[i + 5])
        countries[country_name] = population

    # print_dict(countries)
    file.close()
    return countries

# get_population()
