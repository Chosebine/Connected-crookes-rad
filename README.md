# Connected-crookes-rad
## Projet d'internet des objets pratique : un Radiomètre de Crookes connectés. 

Objectif  * Créer un dispositif de surveillance d'un système dynamique
            * Expérimenter directement les concepts liés à l'échantillonage
            * Utiliser les méthodes de'aquisition et traitement de données et présenter les résultats à un opérateur
            


** Matériel **

* Capteur de luminosité : AMS TSL2591 (https://ams.com/documents/20143/36005/TSL2591_DS000338_6-00.pdf )
    * Fonctionnalités requises :
        * Très vaste plage dynamique (600M:1)
            *   Étant donné que le radiomètre de Crookes peut être placé aussi bien sous un ciel nuageux (0.2 Hz)  qu'en plein soleil(3 Hz et plus , le                       capteur de luminosité doit pouvoir s'adapter à une très grande plage de sensibilité.
        * Temps de réponse "rapide" (100 ms)
            *   Afin de déterminer la vitesse de rotation du radiomètre, le capteur mesure la variation de lumière réfléchie par le radiomètre. Un temps d'intégration de 100 ms correspond à une fréquence d'échantillonage de 10Hz, ce qui correspond à une fréquence mesurable de 5 Hz en vertu du théorème de Nyquist-Shannon.
        * digital (I²C)
            *  Aucune raison d'aller vers l'analogue dans ce cas çi.
                

* Aquisition de données : Rasperry Pi Pico (https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
    *   Fonctionnalités requises :
        * Digital (I²C)     
        * Alimentation et communication par port micro-usb 

* Traitement et diffusion de données : Raspberry pi 4
      *   Le Raspberri pi possède une inferface I²C, il est tout à fait possible d'éliminer le Raspberry pi Pico et utiliser le capteur branché                      directement au Raspberry pi.(la seule véritable raison est que je voulais faire un projet avec mon nouveau Raspberry pi pico! ¯\_(ツ)_/¯ )   
 
 ** Logiciel **
 
      * Raspberri Pi Pico (aquisition de données)
         * Circuit-python : l'interface intéractive et la simplicité du déploiement ont orientés mon choix dans ce cas çi.
 
      * Raspberri pi 4 (traitement et diffusion de données)
      
      *   Serveur Jupyter, ce qui permet d'utiliser les librairies courantes du domaine scientifique  (scipy, numpy, pandas, etc.)
      *   Le noyau  utilisé par Jupyter peut être facilement changé pour R, ce qui permet d'utiliser ses puissants outils d'analyse. (expérimentation future de modèle ARIMA de série de données en autre)
      
      *   Thingsboard, plateforme de gestion d'objets connectés, d'aquisition et analyse de données. (https://thingsboard.io/)
          * Logiciel libre
          * Prend en charge l'auto-hébergement (cloud $$$ non nécéssaire)
         
