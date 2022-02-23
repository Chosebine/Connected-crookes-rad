from io import BufferedRandom
from numpy import datetime64, full, int64
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.tools.datetimes import to_datetime
import serial as ser
import pandas as pd


connex = ser.Serial('/dev/ttyACM0',115200)  # open serial port
old_lux=-1

old_infrared=-1
old_visible=-1
old_full_spectrum=-1
buffsize = 1000

buff = pd.DataFrame(columns=['lux','delta_lux' ,'infrared','delta_infrared','visible','delta_visible','full_spectrum','delta_full_spectrum','date'])
buff['date'] = pd.to_datetime(buff['date'])
buff['lux'] = pd.to_numeric(buff['lux'])
buff['delta_lux'] = pd.to_numeric(buff['delta_lux'])

buff['infrared'] = pd.to_numeric(buff['infrared'])
buff['delta_infrared'] = pd.to_numeric(buff['delta_infrared'])

buff['visible'] = pd.to_numeric(buff['visible'])
buff['delta_visible'] = pd.to_numeric(buff['delta_visible'])

buff['full_spectrum'] = pd.to_numeric(buff['full_spectrum'])
buff['delta_full_spectrum'] = pd.to_numeric(buff['delta_full_spectrum'])
buff.set_index(['date'])

while True:
    
    
    for a in range(buffsize):
        raw_capture = connex.readline()
        raw_capture = raw_capture.decode('utf8')
        raw_capture = raw_capture.split(',')
        
        lux = float(raw_capture[0])
        infrared = int(raw_capture[1])
        visible = int(raw_capture[2])
        full_spectrum = int(raw_capture[3])

        delta_lux=round(lux-old_lux,3)
        delta_infrared=round(infrared-old_infrared,3)
        delta_visible=round(visible-old_visible,3)
        delta_full_spectrum=round(full_spectrum-old_full_spectrum,3)
        
        clean_data = pd.DataFrame([[lux,delta_lux,infrared,delta_infrared,visible,delta_visible,full_spectrum,delta_full_spectrum,  pd.to_datetime(
        pd.Timestamp.now())]], columns=['lux','delta_lux' ,'infrared','delta_infrared','visible','delta_visible','full_spectrum','delta_full_spectrum', 'date'])
        buff = pd.concat([buff, clean_data])
        old_lux=lux
        old_infrared=infrared
        old_visible= visible
        old_full_spectrum= full_spectrum

    print(pd.Timestamp.now(),'\n',clean_data)
    #print(buff.dtypes)
    buff.set_index('date')
    store = pd.HDFStore('data.h5', mode='a',complevel=9)
    store.append(key='date', value=buff, format='t',  data_columns=True)
    store.close()
    buff=buff.iloc[0:0]
connex.close()
