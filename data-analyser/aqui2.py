from io import BufferedRandom
from numpy import datetime64, int64
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.tools.datetimes import to_datetime
import serial as ser
import pandas as pd


connex = ser.Serial('/dev/ttyACM0',115200,)  # open serial port

while True:
 

    bla = connex.readline()
    bla = bla.decode('utf8')
    bla = bla.split(',')
    
    #print(lux,varLux,temp,gaz,humid,press)
    #shit = [lux,temp, gaz, humid,press]
    
    print(bla)
    #print(buff.dtypes)
    
connex.close()
