import bme680
from datetime import datetime

sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

def read_all():
    sensor.get_sensor_data()
    
    return sensor.data.humidity, sensor.data.pressure, sensor.data.temperature, sensor.data.gas_resistance

def human_report():
    sensor.get_sensor_data()
    
    time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    temp = "%.2f" % round((sensor.data.temperature * 1.8) + 32 , 2) # C to F conversion: (temp * 1.8) + 32
    humidity = "%.2f" % round(sensor.data.humidity,2 )
    pressure = "%.2f" % round(sensor.data.pressure, 2)
    gas = sensor.data.gas_resistance
    
    print(f"[{time}] Temperature: {temp}°F, Humidity: {humidity}% rH, Pressure: {pressure} hPa, Gas Resistance {gas} Ohms")
