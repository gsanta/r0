import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)
#gpio.setup(32, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
pwm1 = gpio.PWM(12, 50)
pwm1.start(50)
#pwm2 = gpio.PWM(32, 1)
#pwm2.start(100)
gpio.output(7, False)
gpio.output(11, True)
gpio.output(13, True)
gpio.output(15, False)

time.sleep(3)
gpio.cleanup()
