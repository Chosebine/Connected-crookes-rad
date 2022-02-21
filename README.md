# Connected-crookes-rad
## Mon projet de radiomètre de Crooke connecté

** Matériel **

* senseur optique :  AMS TSL2591 (https://ams.com/documents/20143/36005/TSL2591_DS000338_6-00.pdf )
    * feature nécessaire:
        * Très grand dynamic range (600M:1)
        * Temps d'intégration rapide (100 ms)
        * digital (I²C)

* Collecteur de données : Rasperry pi pico (https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
    *   feature nécessaire:
        * Digital input (I²C)
        * USB/WiFi input output

* Analyseur de données : Raspberry pi 4
    *   USB/WiFi input
    *   assez puissant pour analyser et présenter les données (Jupyter Notebook)
    



