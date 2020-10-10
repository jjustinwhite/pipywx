import bme280
import smbus2
from time import sleep

ADAFRUIT_BME280_I2C_ADDRESS = 0x77

port = 1
address = ADAFRUIT_BME280_I2C_ADDRESS
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)


def collect_sample():
    return bme280.sample(bus, address, calibration_params)

def temperature():
    return collect_sample.temperature

def humidity():
    return collect_sample.humdity
    
def pressure():
    return collect_sample.pressure

def read_all():
    data = collect_sample()
    return data.humidity, data.pressure, data.temperature

def human_report():
    data = collect_sample()
    time = data.timestamp.strftime("%m/%d/%Y %H:%M:%S")
    temp = "%.2f" % round((data.temperature * 1.8) + 32 , 2) # C to F conversion: (temp * 1.8) + 32
    humidity = "%.2f" % round(data.humidity,2 )
    pressure = "%.2f" % round(data.pressure, 2)
    
    print(f"[{time}] Temperature: {temp}°F, Humidity: {humidity}% rH, Pressure: {pressure} hPa")

def poll_report(type, frequency=1):
    while 1 < 2:
        if type == "human":
            human_report()
        elif type == "machine":
            read_all()
            
        sleep(frequency)