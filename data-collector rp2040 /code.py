

# Initialize the sensor.
import time
import board
import busio
import adafruit_tsl2591

# Lock the I2C device before we try to scan
i2cEnv = busio.I2C(board.GP1, board.GP0)
while not i2cEnv.try_lock():
    pass
# Print the addresses found once
print("I2C addresses found:", [hex(device_address) for device_address in i2cEnv.scan()])

# Unlock I2C now that we're done scanning.
i2cEnv.unlock()
sensor = adafruit_tsl2591.TSL2591(i2cEnv)


sensor.gain = adafruit_tsl2591.GAIN_LOW
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

delayLight=0.1
lastLight=-1
lux = -1
infrared = -1
visible = -1    
full_spectrum = -1


while True:
    now=time.monotonic()
    if now >= lastLight + delayLight:
        lux = sensor.lux
        infrared = sensor.infrared
        visible = sensor.visible    
        full_spectrum = sensor.full_spectrum
        lastLight = now
        print("{:4.2f}".format(lux)+','+"{:4}".format(infrared)+','+"{:8}".format(visible)+','+"{:8}".format(full_spectrum))