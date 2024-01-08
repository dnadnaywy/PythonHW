import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'student',
    'port': '5432'
}

connection = psycopg2.connect(**db_params)


def get_top10_population():
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, population FROM countries ORDER BY population::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_top10_density():
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, density FROM countries ORDER BY density::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_top10_area():
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, area FROM countries ORDER BY area::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_specific_language(language):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name FROM countries WHERE language LIKE %s;"
            cursor.execute(select_query, ('%' + language + '%',))
            rows = cursor.fetchall()

    return rows


def get_specific_time_zone(time_zone):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name FROM countries WHERE time_zone LIKE %s;"
            cursor.execute(select_query, ('%' + time_zone + '%',))
            rows = cursor.fetchall()

    return rows


def get_data_about_country(country):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, capital, population, density, area, neighbours, language, time_zone, government FROM countries WHERE name LIKE %s;"
            cursor.execute(select_query, ('%' + country + '%',))
            rows = cursor.fetchall()

    return rows
