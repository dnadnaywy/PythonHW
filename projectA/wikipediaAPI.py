from flask import Flask, request, jsonify
import extract_from_database

app = Flask(__name__)


@app.route('/country', methods=['GET'])
def get_data():
    """
    Rezumat:

    Alte detalii(argumente)
    :return:
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
    return jsonify(extract_from_database.get_top10_population())


@app.route('/top10_area', methods=['GET'])
def get_area():
    return jsonify(extract_from_database.get_top10_area())


@app.route('/language', methods=['GET'])
def get_language():
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
    param = request.args.get('param')

    print(param)
    countries = extract_from_database.get_specific_government(param)
    if countries == []:
        countries = 'Government not found. Only types of government from wikipedia: Absolute, Constitutional, Provisional, Republic.'
    response_data = {
        'param': param,
        'result': countries,
    }

    return jsonify(response_data)


@app.route('/top10_density', methods=['GET'])
def get_top10_density():
    countries = extract_from_database.get_top10_density()
    return jsonify(countries)


if __name__ == '__main__':
    app.run(debug=True)
