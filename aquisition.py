from numpy import datetime64, full, int64
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.tools.datetimes import to_datetime
import serial as ser
import pandas as pd
import os

# Déclaration de variable
old_lux=-1
gain_level=-1
old_infrared=-1
old_visible=-1
old_full_spectrum=-1
buffsize = 1000
delay_thingsboard = 0

# Connexion au port série, création de Dataframe Pandas pour conserver les données du tampon en mémoire jusqu'à la sauvegarde sur fichier

connex = ser.Serial('/dev/ttyACM0',115200)  

buff = pd.DataFrame(columns=['lux','delta_lux' ,'infrared','delta_infrared','visible','delta_visible','full_spectrum','delta_full_spectrum','gain_level','date'])
buff['date'] = pd.to_datetime(buff['date'])
buff['lux'] = pd.to_numeric(buff['lux'])
buff['delta_lux'] = pd.to_numeric(buff['delta_lux'])

buff['infrared'] = pd.to_numeric(buff['infrared'])
buff['delta_infrared'] = pd.to_numeric(buff['delta_infrared'])

buff['visible'] = pd.to_numeric(buff['visible'])
buff['delta_visible'] = pd.to_numeric(buff['delta_visible'])

buff['full_spectrum'] = pd.to_numeric(buff['full_spectrum'])
buff['delta_full_spectrum'] = pd.to_numeric(buff['delta_full_spectrum'])
buff['gain_level'] = pd.to_numeric(buff['gain_level'])
buff.set_index(['date'])

# La Dataframe contient 10 colonnes dont 9 de données et un timestamp.
# Consulter le specsheets du capteur pour avoir plus d'information sur le format et sens
while True:
    
    
    for a in range(buffsize):                       # Lecture et décodage de l'information reçu du Raspberry Pi Pico
        raw_capture = connex.readline()
        raw_capture = raw_capture.decode('utf8')
        split_capture = raw_capture.split(',')
        
        
        if len(raw_capture)>10:
            try:
                lux = float(split_capture[0])
                infrared = int(split_capture[1])
                visible = int(split_capture[2])
                full_spectrum = int(split_capture[3])
                gain_level = int(split_capture[4])
                delta_lux=round(lux-old_lux,3)
                delta_infrared=round(infrared-old_infrared,3)
                delta_visible=round(visible-old_visible,3)
                delta_full_spectrum=round(full_spectrum-old_full_spectrum,3)
            
                clean_data = pd.DataFrame([[lux,delta_lux,infrared,delta_infrared,visible,delta_visible,full_spectrum,delta_full_spectrum,gain_level,pd.to_datetime(
                pd.Timestamp.now())]], columns=['lux','delta_lux' ,'infrared','delta_infrared','visible','delta_visible','full_spectrum','delta_full_spectrum','gain_level', 'date'])
                buff = pd.concat([buff, clean_data])    # Sauvegarde des données dans la mémoire tampon
                old_lux=lux                             # Actualisation des variables utilisé pour calculer les deltas
                old_infrared=infrared
                old_visible= visible
                old_full_spectrum= full_spectrum
                delay_thingsboard+=1
                
                if delay_thingsboard % 20 == 0:       # La fréquence d'actualisation de la plateforme Thingsboard est moins fréquente (0.5 Hz) afin de ne pas surcharger le Rapsberry pi.             
                    data = '"{\\"lux\\":'+str(lux)+', \\"infrared\\": '+str(infrared)+ ', \\"visible\\": '+str(visible)+', \\"full spectrum\\": '+str(full_spectrum)+', \\"gain_level\\": '+str(gain_level)+'}"'
                    line = "curl -k  -X POST -d " + data +  " https://localhost:8080/api/v1/TOKEN_DE_SÉRCURITE/telemetry --header \"Content-Type:application/json\""
                    os.system(line)  # L'utilisation de Curl pour faire la requête POST est un gros dirty hack, la prochaine étape sera de faire la requête HTTP à la main.
                    
            except RuntimeError:
                break
    
    print(pd.Timestamp.now(),'\n',clean_data) # Affichage facultatif pour fin de surveillance.
    
    buff.set_index('date')
    store = pd.HDFStore('~/crooke/code/data.h5', mode='a',complevel=9)  # Sauvegarde des donnés tampon sur fichier
    store.append(key='date', value=buff, format='t',  data_columns=True)
    store.close()    
    buff=buff.iloc[0:0]
connex.close() #Prochaine étape, quitter plus "gracefully"
