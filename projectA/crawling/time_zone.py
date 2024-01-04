import requests
import re

countries_with_time_zones = {}


def crawl_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_code = response.text
        file_path = 'crawling/time_zone.txt'
        try:
            file = open(file_path, 'w', encoding='utf-16')
            file.write(html_code)
            file.close()
        except:
            print("Error at opening file for writing")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


wikipedia_url = 'https://en.wikipedia.org/wiki/List_of_time_zones_by_country'
crawl_wikipedia(wikipedia_url)


def find_the_table():
    file_path = 'crawling/time_zone.txt'
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
    file.close()
    return table


def get_country_name(string):
    match = re.search(r'<a\s+href="/wiki/[^"]+"\stitle="([^"]+)">', string)
    if match:
        country_name = match.group(1)
        return country_name


def get_time_zone(string):
    inside_title_attribute = re.findall(r'title="([^"]+)"', string)

    time_zones = []
    for data in inside_title_attribute:
        if 'UTC' in data:
            time_zones.append(data)
    return time_zones


def get_time_zones():
    table = find_the_table()
    i = 0
    internal_counter = 1
    internal_row = []
    while i < len(table):
        if table[i] == "<tr>\n":
            if internal_row != []:
                country_name = get_country_name(internal_row[0])
                time_zone = get_time_zone(internal_row[2])
                countries_with_time_zones[country_name] = time_zone

            internal_counter = 1
            internal_row = []
        else:
            internal_row.append(table[i])
            internal_counter += 1
        i += 1
    # print(countries_with_time_zones)
    return countries_with_time_zones

# get_time_zones()
