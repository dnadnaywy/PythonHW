import requests
import re

countries_with_areas = {}


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/area.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
# crawl_wikipedia(wikipedia_url)


def get_country(string):
    pattern = re.compile(r'<td>.*?title="([^"]+)".*?>([^<]+)</a>(?: \([^)]+\))?</(?:td|i|span)>')

    # Match the pattern in the input string
    match = pattern.search(string)

    # Extract the country name from the matched groups
    if match:
        return match.group(2)
    else:
        return "NO MATCH FOUND"


def get_area(string):
    pattern = r'<td>([\d,.]+)\s*\(\s*([\d,.]+)\s*\)</td>'

    match = re.search(pattern, string)
    if match:
        number1 = float(match.group(1).replace(',', ''))
        return number1
    else:
        return "NUMBER NOT FOUND"


def get_area_special(string):
    pattern = r'<td style="text-align:right">([\d,]+) \(([\d,]+(?:\.\d+)?)\)</td>'

    match = re.search(pattern, string)

    if match:
        number = match.group(1).replace(',', '')
        return number
    else:
        return "NUMBER NOT FOUND"


def get_country_special(string):
    pattern = r'<a[^>]*\s*title="([^"]*)"[^>]*>.*?</a></td>'

    match = re.search(pattern, string)

    if match:
        country_name = match.group(1)
        return country_name
    else:
        return "NO COUNTRY FOUND"


def get_areas():
    file_path = 'crawling/area.txt'
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

    table = table[25:]
    # print(table)
    i = 0
    internal_counter = 1
    internal_row = []
    while i < len(table):
        if table[i] == "<tr>\n":
            if internal_row != []:
                if internal_counter == 9:
                    country = get_country(internal_row[1])
                    area = get_area(internal_row[2])
                elif internal_counter == 10:
                    country = get_country(internal_row[2])
                    area = get_area(internal_row[3])
                elif internal_counter == 8:
                    country = get_country_special(internal_row[0])
                    area = get_area_special(internal_row[1])
                countries_with_areas[country] = area

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
        i += 1
    # print(countries_with_areas)
    file.close()
    return countries_with_areas


# get_areas()
