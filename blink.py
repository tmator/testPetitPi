#on importe la lib GPIO
import RPi.GPIO as GPIO
#on importe la lib time pour le sleep
import time


#j'utilise la pin 25
laPin=25

#booleen qui dit si ca blinke ou pas
caBlinke=0

#on met les GPIO en mode BCM (donc on utlise la numerotation BCM des pins)
GPIO.setmode(GPIO.BCM)

#on dit que la pin 25 est en sortie
GPIO.setup(laPin, GPIO.OUT)

#on boucle et on clignote
while True:
	if caBlinke==0:
		GPIO.output(laPin, True)
		caBlinke=1
	else:
		GPIO.output(laPin, False)
		caBlinke=0
	time.sleep(0.5)
