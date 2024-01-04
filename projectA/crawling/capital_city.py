import requests
import re

countries_with_capitals = {}


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/capital_city.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_national_capitals'
# crawl_wikipedia(wikipedia_url)


def get_capital_city(string):
    pattern = r'<a\s[^>]*?title="[^"]*"[^>]*>(.*?)</a>'

    match = re.search(pattern, string)

    if match:
        capital_name = match.group(1)
        return capital_name
    else:
        return "Capital name not found."


def get_country(string):
    pattern = r'<a\s[^>]*?title="([^"]*)"[^>]*>.*?</a>'

    match = re.search(pattern, string)

    if match:
        country_name = match.group(1)
        return country_name
    else:
        return "Country name not found."


def get_capital_cities():
    file_path = 'crawling/capital_city.txt'
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

    table = table[8:]

    i = 0
    internal_counter = 1
    internal_row = []
    last_country = []
    last_capital = []
    while i < len(table):
        if table[i] == "<tr>\n":
            if internal_row != []:
                if internal_counter == 5:
                    capital_city = get_capital_city(internal_row[0])
                    country_name = get_country(internal_row[1])
                    last_country = country_name
                    last_capital = capital_city
                    if country_name not in countries_with_capitals.keys():
                        countries_with_capitals[country_name] = [capital_city]
                    else:
                        countries_with_capitals[country_name].append(capital_city)
                elif internal_counter in (3, 4):
                    capital_city = get_capital_city(internal_row[0])

                    if capital_city in ('Northern Cyprus', 'Palestine'):
                        last_country = capital_city
                        capital_city = last_capital
                    if last_country not in countries_with_capitals.keys():
                        countries_with_capitals[country_name] = [capital_city]
                    else:
                        countries_with_capitals[country_name].append(capital_city)

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
            # if table[i] == "</td></tr>\n":
            #     print(internal_row)
        i += 1
    # print(countries_with_capitals)
    file.close()
    return countries_with_capitals


# get_capital_cities()
