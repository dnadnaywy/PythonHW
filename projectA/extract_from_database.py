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
    """
        This function searches for top 10 countries ordered by population in the database

        :return: a top 10 of countries sorted after population
    """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, population FROM countries ORDER BY population::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_top10_density():
    """
        This function searches for top 10 countries ordered by density in the database

        :return: a top 10 of countries sorted after density
    """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, density FROM countries ORDER BY density::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_top10_area():
    """
        This function searches for top 10 countries ordered by area in the database

        :return: a top 10 of countries sorted after area
    """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, area FROM countries ORDER BY area::int DESC LIMIT 10;"
            cursor.execute(select_query)
            rows = cursor.fetchall()

    return rows


def get_specific_language(language):
    """
            This function searches for countries which have the specified language

            :param language: the searched language in the database
            :return: countries which have the specified language
            """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name FROM countries WHERE language LIKE %s;"
            cursor.execute(select_query, ('%' + language + '%',))
            rows = cursor.fetchall()

    return rows


def get_specific_time_zone(time_zone):
    """
        This function searches for countries which have the specified time_zone

        :param time_zone: the searched time_zone in the database
        :return: countries which have the specified time_zone
        """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name FROM countries WHERE time_zone LIKE %s;"
            cursor.execute(select_query, ('%' + time_zone + '%',))
            rows = cursor.fetchall()

    return rows


def get_specific_government(government):
    """
        This function searches for countries which have the specified government

        :param government: the searched government in the database
        :return: countries which have the specified government
        """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name FROM countries WHERE government LIKE %s;"
            cursor.execute(select_query, ('%' + government + '%',))
            rows = cursor.fetchall()

    return rows


def get_data_about_country(country):
    """
    This function searches data about the specified country from the database

    :param country: the searched country in the database
    :return: data about the specified country from the database
    """
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            select_query = "SELECT name, capital, population, density, area, neighbours, language, time_zone, government FROM countries WHERE name LIKE %s;"
            cursor.execute(select_query, ('%' + country + '%',))
            rows = cursor.fetchall()

    return rows
