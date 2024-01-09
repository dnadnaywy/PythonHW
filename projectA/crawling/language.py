import requests
import re

countries_with_languages = {}


def crawl_wikipedia(url):
    """
    Crawl a Wikipedia page and save its HTML content to a file.

    This function sends a GET request to the specified URL, retrieves the HTML content,
    and saves it to a file named 'crawling/language.txt' using UTF-16 encoding.

    :param url: The URL of the Wikipedia page to crawl.

    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/language.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory'
crawl_wikipedia(wikipedia_url)


def find_the_table():
    """
    Find and extract a table from an HTML file.

    This function reads an HTML file, searches for a specific table class,
    and extracts the content of the identified table.

    :return: A list containing the lines of the extracted table.
    """
    file_path = 'crawling/language.txt'
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

    table = table[14:]
    file.close()
    return table


def extract_country_info(html_string):
    """
    Extract the name of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the country name.

    :param string: The HTML string to search for the country name.

    :return: The extracted country name.
    """
    pattern = r'<a[^>]*>([^<]*)</a>'
    match = re.search(pattern, html_string)
    if match:
        country_name = match.group(1)
        return country_name
    else:
        return "No country found."


def get_official_language(string):
    """
    Extract the official language(s) of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the official language(s) of the country.

    :param string: The HTML string to search for the official language(s) of the country.

    :return: The extracted official language(s) of the country.
    """
    i = 2
    something = 0
    # print(string)
    languages = []
    while string[i] != '</td>\n':
        # print(string[i])
        if string[i] != '<td>\n':
            pattern = r'>([^<\n]+)'
            match = re.search(pattern, string[i])
            if match:
                language = match.group(1)
                languages.append(language)
            else:
                something += 1
        i += 1
    return languages

def get_languages():
    """
    Parse and search for all the official languages of the countries in the url from Wikipedia.

    :return: A dictionary containing the official language(s) of each country.
    """
    table = find_the_table()
    i = 0
    internal_counter = 1
    internal_row = []
    while i < len(table):
        if table[i] == "<tr>\n":
            if internal_row != []:
                country_name = extract_country_info(internal_row[0])
                # print(country_name)
                languages = get_official_language(internal_row)
                # print(languages)
                countries_with_languages[country_name] = languages

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
        i += 1
    # print(countries_with_languages)
    return countries_with_languages


get_languages()
