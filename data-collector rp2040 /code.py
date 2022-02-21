

# Initialize the sensor.
import time
import board
import busio
import adafruit_bme680
import usb_cdc
#usb_cdc.enable(console=True, data=True)
import adafruit_tsl2591
# Lock the I2C device before we try to scan
i2cEnv = busio.I2C(board.GP1, board.GP0)
while not i2cEnv.try_lock():
    pass
# Print the addresses found once
print("I2C addresses found:", [hex(device_address) for device_address in i2cEnv.scan()])

# Unlock I2C now that we're done scanning.
i2cEnv.unlock()

#i2cLum = busio.I2C(scl=board.GP17, sda=board.GP16)
#while not i2cEnv.try_lock():
 #   pass
# Create sensor object, communicating over the board's default I2C bus
#from adafruit_bus_device.i2c_device import I2CDevice

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2cEnv)
sensor = adafruit_tsl2591.TSL2591(i2cEnv)
# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1028.05
sensor.gain = adafruit_tsl2591.GAIN_LOW
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS
delayLight=0.01
delayEnv=10
lastLight=-1
lastEnv=-1
lastPrint = -1
delayPrint = 0.1
lux = -1
infrared = -1
visible = -1    #print("Visible light: {0}".format(visible))
full_spectrum = -1
temp=-1
gaz=-1
humid = -1
press = -1


while True:
    now=time.monotonic()
    if now >= lastLight + delayLight:
        lux = sensor.lux
        infrared = sensor.infrared
        visible = sensor.visible    #print("Visible light: {0}".format(visible))
        full_spectrum = sensor.full_spectrum
        lastLight = now
    if now >= lastEnv + delayEnv:
        temp=bme680.temperature
        gaz= bme680.gas
        humid = bme680.relative_humidity
        press = bme680.pressure
        lastEnv=now

    print("{:4.2f}".format(lux)+','+"{:4}".format(infrared)+','+"{:8}".format(visible)+','+"{:8}".format(full_spectrum))
    #if now >= lastPrint + delayPrint:
    #    print(str(lux) +','+ str(temp) +','+str(gaz)+','+str(humid)+','+str(press))
    #    lastPrint=now

