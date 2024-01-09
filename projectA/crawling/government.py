import requests
import re

countries_with_governments = {}


def crawl_wikipedia(url):
    """
    Crawl a Wikipedia page and save its HTML content to a file.

    This function sends a GET request to the specified URL, retrieves the HTML content,
    and saves it to a file named 'crawling/government.txt' using UTF-16 encoding.

    :param url: The URL of the Wikipedia page to crawl.

    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/government.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_system_of_government#List_of_countries'
crawl_wikipedia(wikipedia_url)


def find_the_table():
    """
    Find and extract a table from an HTML file.

    This function reads an HTML file, searches for a specific table class,
    and extracts the content of the identified table.

    :return: A list containing the lines of the extracted table.
    """
    file_path = 'crawling/government.txt'
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

    table = table[11:]
    table = table[:-91]
    file.close()
    return table


def get_country_name(string):
    """
    Extract the name of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the country name.

    :param string: The HTML string to search for the country name.

    :return: The extracted country name.
    """
    country_match = re.search(r'<a\s[^>]*?href="/wiki/([^"]+)"[^>]*>([^<]+)</a>', string)

    if country_match:
        country_name = country_match.group(2)
        return country_name


def get_government(string):
    """
    Extract the government of a country from an HTML string.

    This function uses a regular expression to search for a specific pattern
    in the provided HTML string and extracts the government of the country.

    :param string: The HTML string to search for the government of the country.

    :return: The extracted government of the country.
    """
    match = re.search(r'<td>(\w+)', string)

    if match:
        word_after_td = match.group(1)
        return word_after_td
    else:
        return None


def get_governments():
    """
    Parse and search for all the governments of the countries in the url from Wikipedia.

    :return: A dictionary containing the government of each country.
    """
    table = find_the_table()
    i = 0
    internal_counter = 1
    internal_row = []
    while i < len(table):
        if "<tr" in table[i]:
            if internal_row != []:
                country_name = get_country_name(internal_row[0])
                government = get_government(internal_row[2])
                countries_with_governments[country_name] = government

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
        i += 1
    # print(countries_with_governments)
    return countries_with_governments

# get_governments()
