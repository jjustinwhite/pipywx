# pipywx
A Personal Weather Station (PWS) built using a Raspberry Pi and Python. You can follow along with my progress at https://medium.com/@_jjustinwhite

## Currently Supported Sensors
### BME280 
The [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) is a sensor from Bosch that measures relative humidity, barometric pressure, and ambient temperature. I'm using an [Adafruit](https://www.adafruit.com/product/2652) breakout board that contains this sensor. Communication to happens via I2C.

### CCS811 
The [CCS811](https://cdn-shop.adafruit.com/product-files/3566/3566_datasheet.pdf) is a sensor from AMS providing measurements on Volatile Organic Compounds (VOCs) and equivalent calculated carbon-dioxide (eCO2). I'm using this sensor on an [Adafruit](https://www.adafruit.com/product/3566) breakout board. It's using I2C to communicate. I've read that [this sensor is unreliable with the Raspberry Pi](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/i2c-clock-stretching) due to clock stretching, so I've slowed down the I2C clock to try to remidiate it. In addition, support for temperature readings on this sensor has become deprecated, and it's recommended you take temperature readings from another sensor like the BME280. You can give the CCS811 temperature and humidity data from an external sensor to compute VOCs and eCO2 with high accuracy.
