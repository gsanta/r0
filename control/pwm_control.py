import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

pwm = gpio.PWM(12, 50)
pwm.start(60)

gpio.output(15, False)
gpio.output(13, True)

time.sleep(2)
gpio.cleanup()

