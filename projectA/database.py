import psycopg2
from main import all_countries

countries_data = all_countries

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'student',
    'port': '5432'
}

connection = psycopg2.connect(**db_params)

cursor = connection.cursor()
try:
    for country in countries_data:
        insert_query = """
            INSERT INTO countries (name, capital, population, density, area, neighbours, language, time_zone, government)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(insert_query, (country['country_name'], country['capital_city'], country['population'], country['density'], country['area'], country['neighbours'], country['language'], country['time_zone'],country['government']))

        connection.commit()
    print("Data successfully inserted into countries table.")
except:
    print("Error at insert into database.")

cursor.close()
connection.close()
