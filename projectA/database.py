import psycopg2

db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'student',
    'port': '5432'
}

connection = psycopg2.connect(**db_params)

cursor = connection.cursor()

data_to_insert = {
    'name': 'John Doe'
}

insert_query = """
    INSERT INTO test (name)
    VALUES ('Tavi');
"""

cursor.execute(insert_query, data_to_insert)

connection.commit()

cursor.close()
connection.close()
