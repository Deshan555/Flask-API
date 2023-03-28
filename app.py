from flask import Flask, request, jsonify

import Box_01

import Box_2

import GasValue

import HeatIndex

import Temp

import humidity

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    print(user['name'], user['age'])
    return jsonify("ok")


@app.route('/v01/device/box_01/', methods=['GET'])
def get_Box_01():
    return jsonify(Box_01.sensor_Box1())


@app.route('/v01/device/box_02/', methods=['GET'])
def get_Box_02():
    return jsonify(Box_2.sensor_Box2())


@app.route('/v01/device/humidity/', methods=['POST'])
def humidity_get():
    date = request.get_json()
    return_data = humidity.humidity(date['date'])
    return jsonify(return_data)


@app.route('/v01/device/temperature/', methods=['POST'])
def temperature_get():
    date = request.get_json()
    return_data = Temp.temperature(date['date'])
    return jsonify(return_data)


@app.route('/v01/device/gasValue/', methods=['POST'])
def gasValue_get():
    date = request.get_json()
    return_data = GasValue.gasValue(date['date'])
    return jsonify(return_data)


@app.route('/v01/device/heatIndex/', methods=['POST'])
def heatIndex_get():
    date = request.get_json()
    return_data = HeatIndex.heatIndex(date['date'])
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)