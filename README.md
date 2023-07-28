# 🌐 Flask API for Environmental Sensor Data 🌐

Welcome to our Flask API for accessing environmental sensor data! This API provides endpoints to retrieve information from various sensors, including Box_01, Box_02, humidity, temperature, gasValue, heatIndex, water level, and soil moisture. By integrating this API into your applications, you can access real-time and historical data from these sensors.

𝗧𝗵𝗮𝘁 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗜𝘀 𝗣𝗮𝗿𝘁 𝗢𝗳 : 𝗵𝘁𝘁𝗽𝘀://𝗴𝗶𝘁𝗵𝘂𝗯.𝗰𝗼𝗺/𝗗𝗲𝘀𝗵𝗮𝗻𝟱𝟱𝟱/𝗜𝗢𝗧-𝗦𝗺𝗮𝗿𝘁_𝗙𝗮𝗿𝗺𝗶𝗻𝗴.𝗴𝗶𝘁

📦 Installation and Usage 📦

1. Clone or download this repository to your local machine.
2. Ensure you have Python and Flask installed.
3. Import the necessary modules: Box_01, Box_2, GasValue, HeatIndex, SoilMois, Temp, WaterLvl, and Humidity.
4. Run the Flask application using the following command:

```bash
python app.py
```

5. The API will run on http://0.0.0.0:105/.

📝 Endpoints 📝

1. **GET /v01/device/box_01/**
   - Description: Get data from Box_01 sensor.
   - Usage: Access this endpoint to retrieve sensor data from Box_01.
   - Example Response: JSON data containing Box_01 sensor information.

2. **GET /v01/device/box_02/**
   - Description: Get data from Box_02 sensor.
   - Usage: Access this endpoint to retrieve sensor data from Box_02.
   - Example Response: JSON data containing Box_02 sensor information.

3. **POST /v01/device/humidity/**
   - Description: Get humidity data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve humidity data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing humidity information for the specified date.

4. **POST /v01/device/temperature/**
   - Description: Get temperature data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve temperature data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing temperature information for the specified date.

5. **POST /v01/device/gasValue/**
   - Description: Get gasValue data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve gasValue data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing gasValue information for the specified date.

6. **POST /v01/device/heatIndex/**
   - Description: Get heatIndex data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve heatIndex data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing heatIndex information for the specified date.

7. **POST /v01/device/water-lvl/**
   - Description: Get water level data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve water level data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing water level information for the specified date.

8. **POST /v01/device/soil-moisture/**
   - Description: Get soil moisture data for a specific date.
   - Usage: Send a POST request with a JSON payload containing the "date" field to retrieve soil moisture data for that date.
   - Example Request Payload: `{ "date": "2023-07-28" }`
   - Example Response: JSON data containing soil moisture information for the specified date.

Feel free to use and modify this Flask API to suit your specific needs. We value your feedback and contributions to make this project even better! Happy coding! 😊

[Insert GitHub Repository URL Here]
