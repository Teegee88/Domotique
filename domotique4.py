import RPi.GPIO as GPIO
import mysql.connector
import sys
from mysql.connector import errorcode

#Definition de nos pin
SALON_CHAUFFAGE = 7
CUISINE_CHAUFFAGE = 8
CHAMBRE_CHAUFFAGE = 9
SALON_FENETRE_GAUCHE = 17
SALON_FENETRE_DROITE = 4
CHAMBRE_FENETRE = 22
CUISINE_FENETRE = 27
PORTE_ENTREE = 23
PORTE_INT_GAUCHE = 24
PORTE_INT_DROITE = 25

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SALON_CHAUFFAGE, GPIO.OUT) #Chauffage Salon
GPIO.setup(CHAMBRE_CHAUFFAGE, GPIO.OUT) #Chauffage Chambre
GPIO.setup(CUISINE_CHAUFFAGE, GPIO.OUT) #Chauffage Cuisine
GPIO.setup(10, GPIO.OUT) #Chauffage Exterieur (non utilise)

#GPIO des capteurs d'ouverture
GPIO.setup(SALON_FENETRE_GAUCHE, GPIO.IN)#Fenetre salon gauche
GPIO.setup(SALON_FENETRE_DROITE, GPIO.IN)#Fenetre avant droite 27
GPIO.setup(CHAMBRE_FENETRE, GPIO.IN)#Fenetre chambre 22
GPIO.setup(CUISINE_FENETRE, GPIO.IN)#Fenetre cuisine 27
GPIO.setup(PORTE_ENTREE, GPIO.IN)#
GPIO.setup(PORTE_INT_GAUCHE, GPIO.IN)#
GPIO.setup(PORTE_INT_DROITE, GPIO.IN)#



try:
     while 1:
        def chauffage(piece, state , gpio):
                if state == 'ON' :
                        fenetre(piece, gpio)
                elif state == 'OFF':
                        GPIO.output(gpio, GPIO.LOW)
                else :
                        print "Error"
        def fenetre(piece, gpio):
                if piece=='Salon' :
					fenetreGaucheSalon=GPIO.input(SALON_FENETRE_GAUCHE)
					fenetreDroiteSalon=GPIO.input(SALON_FENETRE_DROITE)
					porteEntree=GPIO.input(PORTE_ENTREE)
					#si un des trois est ouvert on éteint le chauffage
					if fenetreGaucheSalon or fenetreDroiteSalon or porteEntree:
						GPIO.output(gpio, GPIO.LOW)
					else:
						GPIO.output(gpio, GPIO.HIGH)
				if piece=='Chambre' :
					fenetreChambre=GPIO.input(CHAMBRE_FENETRE)
					if fenetreChambre:
						GPIO.output(gpio, GPIO.LOW)
					else:
						GPIO.output(gpio, GPIO.HIGH)
				if piece=='Cuisine' :
					fenetreCuisine=GPIO.input(CUISINE_FENETRE)
					if fenetreCuisine:
						GPIO.output(gpio, GPIO.LOW)
					else:
						GPIO.output(gpio, GPIO.HIGH)

        con = mysql.connector.connect(host='172.17.10.59', user='java', password='javapwd', database='domotique')


        cur = con.cursor()
        query = "SELECT PIECE,CHAUFFAGE FROM PIECE"
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:

                if row[0] == 'Salon'  :
                        chauffage(row[0], row[1] , SALON_CHAUFFAGE)
                        print(row[1])
                elif row[0] == 'Chambre' :
                        chauffage(row[0], row[1] , 9)

                elif row[0] == 'Cuisine' :
                        chauffage(row[0], row[1] , 8)

                elif row[0] == 'Exterieur':
                        chauffage(row[0], row[1] , 10)
                else :
                         print "Error"



except mysql.connector.Error as err:
    print "La connexion echouee"

else:
    con.close()
