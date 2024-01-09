from flask import Flask, request, jsonify
import extract_from_database

app = Flask(__name__)


@app.route('/country', methods=['GET'])
def get_data():
    """
        Get data about a specific country.

        This endpoint allows you to retrieve information about a specific country
        by providing the country name as a query parameter.

        :return: A JSON response containing information about the country.
                 If the country is not found, the result will be 'Country not found.'
    """
    param = request.args.get('country')

    data = extract_from_database.get_data_about_country(param)
    if data == []:
        data = 'Country not found.'
    response_data = {
        'country': param,
        'result': data,
    }

    return jsonify(response_data)



@app.route('/top10_population', methods=['GET'])
def get_population():
    """
    Get the top 10 countries by population.

    This endpoint allows you to retrieve information about the top 10 countries
    with the highest population from the database.

    :return: A JSON response containing information about the top 10 countries by population.
    """
    return jsonify(extract_from_database.get_top10_population())


@app.route('/top10_area', methods=['GET'])
def get_area():
    """
    Get the top 10 countries by area.

    This endpoint allows you to retrieve information about the top 10 countries
    with the largest area from the database.

    :return: A JSON response containing information about the top 10 countries by area.
    """
    return jsonify(extract_from_database.get_top10_area())


@app.route('/language', methods=['GET'])
def get_language():
    """
    Get countries that speak a specific language.

    This endpoint allows you to retrieve information about countries that speak
    a specific language by providing the language name as a query parameter.

    :return: A JSON response containing information about countries speaking the specified language.
             If the language is not found, the result will be 'Language not found. Try again with a syntax for your language like this: English'
    """
    param = request.args.get('param')

    countries = extract_from_database.get_specific_language(param)
    if countries == []:
        countries = 'Language not found. Try again with a syntax for your language like this: English'
    response_data = {
        'param': param,
        'result': countries,
    }

    return jsonify(response_data)


@app.route('/time_zone', methods=['GET'])
def get_time_zone():
    """
    Get countries in a specific time zone.

    This endpoint allows you to retrieve information about countries in a specific
    time zone by providing the time zone identifier as a query parameter.

    :return: A JSON response containing information about countries in the specified time zone.
             If the time zone is not found, the result will be 'Time zone not found. Try again with a syntax for your
             time zone like this: UTC%2B02:00 or %2B02 or −2:0'
    """
    param = request.args.get('param')

    print(param)
    countries = extract_from_database.get_specific_time_zone(param)
    if countries == []:
        countries = 'Time zone not found. Try again with a syntax for your time zone like this: UTC%2B02:00 or %2B02 or −2:0(for − works)'
    response_data = {
        'param': param,
        'result': countries,
    }

    return jsonify(response_data)


@app.route('/government', methods=['GET'])
def get_government():
    """
    Get countries with a specific type of government.

    This endpoint allows you to retrieve information about countries with a specific
    type of government by providing the government type as a query parameter.

    :return: A JSON response containing information about countries with the specified type of government.
             If the government type is not found, the result will be 'Government not found. Only types of government
             from Wikipedia: Absolute, Constitutional, Provisional, Republic.'
    """
    param = request.args.get('param')

    print(param)
    countries = extract_from_database.get_specific_government(param)
    if countries == []:
        countries = 'Government not found. Only types of government from Wikipedia: Absolute, Constitutional, Provisional, Republic.'
    response_data = {
        'param': param,
        'result': countries,
    }

    return jsonify(response_data)


@app.route('/top10_density', methods=['GET'])
def get_top10_density():
    """
    Get the top 10 countries by density.

    This endpoint allows you to retrieve information about the top 10 countries
    with the highest density from the database.

    :return: A JSON response containing information about the top 10 countries by density.
    """
    countries = extract_from_database.get_top10_density()
    return jsonify(countries)


if __name__ == '__main__':
    app.run(debug=True)
