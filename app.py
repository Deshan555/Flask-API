from flask import Flask, request, jsonify

import Box_01, Box_2, GasValue, HeatIndex, SoilMois, Temp, WaterLvl, humidity

app = Flask(__name__)


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


@app.route('/v01/device/water-lvl/', methods=['POST'])
def water_lvl():
    date = request.get_json()
    return_data = WaterLvl.waterLvl(date['date'])
    return jsonify(return_data)


@app.route('/v01/device/soil-moisture/', methods=['POST'])
def soil_moisture():
    date = request.get_json()
    return_data = SoilMois.soilMoisture(date['date'])
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
