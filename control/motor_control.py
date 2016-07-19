import RPi.GPIO as gpio
import time


def init():
    print "in init"
    gpio.setmode(gpio.BOARD)
    gpio.setup(32, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    pwm1 = gpio.PWM(12, 50)
    pwm1.start(60)
    print "init vege"

def forward():
    init()
    print "init utan"
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(3)
    return "forward"

def reverse():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    return "reverse"

def turn_left():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    return "turn left"

def turn_right():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    return "turn right"

def stop_motor():
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    return "motor stops"

forward()
