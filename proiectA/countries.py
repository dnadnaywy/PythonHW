from time import sleep
import countries_links
import project
from crawling import capital_city

all_countries = []
error = []

if __name__ == '__main__':
    links = countries_links.get_countries_links()
    for i in range(len(links)):
        link = links[i]
        try:
            country_data = project.crawl_wikipedia('https://en.wikipedia.org' + link)
            all_countries.append(country_data)
            print(country_data)
            # sleep(3)
        except:
            error.append(link)
            print('Some error occurred at link: ' + link)
    print("Errors: " + str(error))
