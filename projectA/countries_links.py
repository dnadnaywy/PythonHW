import requests
import re


def crawl_wikipedia(url):
    """
    Crawl a Wikipedia page and save its HTML content to a file.

    This function sends a GET request to the specified URL, retrieves the HTML content,
    and saves it to a file named 'countries_links.txt' using UTF-16 encoding.

    :param url: The URL of the Wikipedia page to crawl.

    :return: None
    """
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'countries_links.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states'
# crawl_wikipedia(wikipedia_url)

countries_with_link = []


def get_country_link(string):
    """
    Extract a country link from an HTML string.

    This function searches for a country link in the provided HTML string using
    a regular expression. If a match is found, the extracted link is returned.

    :param string: The HTML string to search for the country link.

    :return: The extracted country link.
    """
    match = re.search(r'href="/wiki/([^"]+)"', string)

    if match:
        link = match.group(1)
        return link
    else:
        return "Link not found."


def get_countries_links():
    """
    Parse and search for all the country links in the url from Wikipedia.

    :return: A dictionary containing links about all the countries.
    """
    file_path = 'countries_links.txt'
    file = open(file_path, 'r', encoding='utf-16')
    html_line = file.readline()
    table = []
    in_table = False
    while html_line:
        html_line = file.readline()
        if '<table class="sortable wikitable' in html_line:
            in_table = True
        if '</table' in html_line and in_table is True:
            in_table = False

        if in_table:
            table.append(html_line)

    table = table[11:]
    table = table[:-112]
    table.append('</td></tr>')
    for i in range(0, len(table), 9):
        try:
            country_link = get_country_link(table[i + 1])
            countries_with_link.append(country_link)

            while table[i + 8] != '</td></tr>\n':
                table = table[:i + 8] + table[i + 9:]
        except:
            error = "Table too short, anyway"

    file.close()
    return countries_with_link

# get_countries_links()
