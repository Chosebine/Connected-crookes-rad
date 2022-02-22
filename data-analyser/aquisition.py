from io import BufferedRandom
from numpy import datetime64, int64
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.tools.datetimes import to_datetime
import serial as ser
import pandas as pd


connex = ser.Serial('/dev/ttyACM0',115200)  # open serial port
oldLux=-1
while True:
    buffsize = 3000
    buff = pd.DataFrame(columns=['lux','varlux' ,'date'])
    buff['date'] = pd.to_datetime(buff['date'])
    buff['lux'] = pd.to_numeric(buff['lux'])
    buff['varlux'] = pd.to_numeric(buff['varlux'])
    buff.set_index(['date'])
    
    for a in range(buffsize):
        bla = connex.readline()
        bla = bla.decode('utf8')
        bla = bla.split(',')
        lux = float(bla[0])
        varLux=round(lux-oldLux,3)
        shit = pd.DataFrame([[lux,varLux,  pd.to_datetime(
        pd.Timestamp.now())]], columns=['lux','varlux', 'date'])
        buff = pd.concat([buff, shit])
        oldLux=lux
    print(pd.Timestamp.now(),shit)
    #print(buff.dtypes)
    buff.set_index('date')
    store = pd.HDFStore('data.h5', mode='a',complevel=9)
    store.append(key='date', value=buff, format='t',  data_columns=True)
    store.close()
connex.close()
