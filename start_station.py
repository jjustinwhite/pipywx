from sensors import bme280_sensor
from sensors import bme680_sensor
from influxdb import InfluxDBClient
from time import sleep
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

host = "localhost"
port = 8086
user = os.environ.get("influxdb-user")
password = os.environ.get("influxdb-password")
dbname = "weather"
interval = 60

client = InfluxDBClient(host, port, user, password, dbname)

def record_bme680():
    measurement = "bme680"
    location = "office"
    humidity, pressure, temperature, gas = bme680_sensor.read_all()
    time = datetime.utcnow()
    print(f"[{time}] Temp: {temperature}, Humidity {humidity}, Pressure: {pressure}, Gas: {gas}")
    
    data = [
        {
            "measurement": measurement,
                "tags": {
                    "location": location,
                },
            "time": time,
            "fields": {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure,
                "gas": gas
            }
        }
    ]
    client.write_points(data)

def record_bme280():
    measurement = "bme280"
    location = "office"
    humidity, pressure, temperature = bme280_sensor.read_all()
    time = datetime.utcnow()
    print(f"[{time}] Temp: {temperature}, Humidity {humidity}, Pressure: {pressure}")
    
    data = [
        {
            "measurement": measurement,
                "tags": {
                    "location": location,
                },
            "time": time,
            "fields": {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure
            }
        }
    ]
    client.write_points(data)

while True:
    record_bme280()
    record_bme680()
    sleep(60)


