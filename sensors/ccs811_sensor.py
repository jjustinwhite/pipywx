import busio
import adafruit_ccs811
import time
from board import *

print("Starting up CCS811 Sensor")
i2c_bus = busio.I2C(SCL, SDA)
sensor = adafruit_ccs811.CCS811(i2c_bus)

while True:
    try:
        if sensor.data_ready:
            timestamp = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
            print(f"[{timestamp}] C02: {sensor.eco2} ppm, TVOC: {sensor.tvoc} ppm, Temperature: {round(sensor.temperature)}°C")
    except OSError as error:
        print(error)
