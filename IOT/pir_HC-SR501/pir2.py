import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4 
GPIO.setup(PIR_PIN, GPIO.IN)

def logger(i_strCand):
	"optional comment line"
	f = open('pir_HC-SR501', 'w')
	f.write(i_strCand)
	f.close
	return


def MOTION(PIR_PIN):
	"comment"
	logger(str(datetime.datetime.now()))
        print str(datetime.datetime.now()) + "Motion Detected"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               print " Quit"
               GPIO.cleanup()

