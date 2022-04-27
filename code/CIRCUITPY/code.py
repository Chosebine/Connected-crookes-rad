
import time
import board
import busio
import adafruit_tsl2591


# Création de l'interface I2C 

i2cEnv = busio.I2C(board.GP1, board.GP0, frequency=100000)
while not i2cEnv.try_lock():
    pass

i2cEnv.unlock()

sensor = adafruit_tsl2591.TSL2591(i2cEnv) #connexion au capteur à l'aide de l'interface I2C

#déclaration de constantes et variables
gain_lst=[adafruit_tsl2591.GAIN_LOW,adafruit_tsl2591.GAIN_MED,adafruit_tsl2591.GAIN_HIGH,adafruit_tsl2591.GAIN_MAX]
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS


delayLight=0.1
lastLight=-1
lastgain=-1
lux = -1
infrared = -1
visible = -1    
full_spectrum = -1
gain_lvl=3
sensor.gain=gain_lst[gain_lvl]


while True:
    now=time.monotonic()
    
    if now >= lastLight + delayLight:
        try:    
            lux = sensor.lux           #lecture du capteur
            infrared = sensor.infrared
            visible = sensor.visible    
            full_spectrum = sensor.full_spectrum
            lastLight = now            
            print("{:4.2f}".format(lux)+','+"{:4}".format(infrared)+','+"{:8}".format(visible)+','+"{:8}".format(full_spectrum)+','+"{:1}".format(gain_lvl)) # sortie des données en format CSV
            if infrared<250:        # Système de gestion du gain (AGC)n
                if gain_lvl<3:      # rudimentaire mais fonctionnel
                    gain_lvl=gain_lvl+1
                    sensor.gain = gain_lst[gain_lvl]
                    time.sleep(0.2)                                
        except RuntimeError:            
            if gain_lvl>0:                        
                gain_lvl=gain_lvl-1
                sensor.gain = gain_lst[gain_lvl]
            time.sleep(0.2) # pause nécéssaire suite au changement de gain                                
                            
