# Connected-crookes-rad
## Projet d'internet des objets : un Radiomètre de Crookes connectés. 
------
## Objectifs 

* Créer un dispositif de surveillance d'un système dynamique
* Expérimenter directement les concepts liés à l'échantillonage
* Utiliser les méthodes de'aquisition et traitement de données et présenter les résultats à un opérateur
            

------
 ### Matériel 



1. Capteur de luminosité : AMS TSL2591 (https://ams.com/documents/20143/36005/TSL2591_DS000338_6-00.pdf )
   #### Fonctionnalités requises :
      * Très vaste plage dynamique (600M:1)
          * Étant donné que le radiomètre de Crookes peut être placé aussi bien sous un ciel nuageux (0.2 Hz)  qu'en plein soleil(3 Hz et plus , le                       capteur de luminosité doit pouvoir s'adapter à une très grande plage de sensibilité.
        
        
      * Temps de réponse "rapide" (100 ms)
          * Afin de déterminer la vitesse de rotation du radiomètre, le capteur mesure la variation de lumière réfléchie par le radiomètre. Un temps d'intégration de 100 ms correspond à une fréquence d'échantillonage de 10Hz, ce qui correspond à une fréquence mesurable de 5 Hz en vertu du théorème de Nyquist-Shannon.
    * digitale (I²C)
      * Aucune raison d'aller vers l'analogue dans ce cas çi.
      



2. Aquisition de données : Rasperry Pi Pico (https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
    #### Fonctionnalités requises :
      * Digitale (I²C)  
         
      * Alimentation et communication par port micro-usb 



3. Traitement et diffusion de données : Raspberry pi 4
      *   Le Raspberri pi possède une inferface I²C, il est tout à fait possible d'éliminer le Raspberry pi Pico et utiliser le capteur branché                      directement au Raspberry pi.(la seule véritable raison est que je voulais faire un projet avec mon nouveau Raspberry pi pico! :)   
 
 ### Logiciel
 
1. CircuitPython : 
    * Interface intéractive simplifiant l'expérimentation
    * Simplicité du déploiement
    * Librairie du capteur TSL2591 disponible en CircuitPython
           
2. Serveur Jupyter : 
    * L'accès aux librairies courantes du domaine scientifique (scipy, numpy,.etc) permet de lire,traiter et présenter les données enregistrés.
    * Possibilité d'installer un noyau R en complément
         
3. Plateforme de gestion d'objets connectés Thingsboard.
    * Permet l'affichage en temps réel de l'état des objets
    * Prends en charge nativement plusieurs widgets de présentation des données (graphique,jauge etc.)
    * Permet l'auto-hébergement. (ne nécéssite pas de service d'infonuagique)
         
      
              
