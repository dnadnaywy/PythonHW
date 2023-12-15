import requests
import re


def crawl_wikipedia(url):
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
    match = re.search(r'href="(/wiki/[^"]+)"', string)

    if match:
        link = match.group(1)
        return link
    else:
        return "Link not found."


def get_countries_links():
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
