import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

trigPin = 16
echoPin = 18

print "Distance Measurement in Progress"

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.output(trigPin, False)
print "Waiting For Sensor To Settle"

time.sleep(2)

GPIO.output(trigPin, True)
time.sleep(0.00001)
GPIO.output(trigPin, False)

while GPIO.input(echoPin) == 0:
    pulseStart = time.time()

while GPIO.input(echoPin) == 1:
    pulseEnd = time.time()

pulseDuration = pulseEnd - pulseStart
distance = pulseDuration * 17150
distance = round(distance, 2)

print "Distance: ", distance, "cm"

GPIO.cleanup()
