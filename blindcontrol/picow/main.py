from machine import Pin, PWM, Timer, ADC
from micropython import schedule
from time import ticks_ms, ticks_us, sleep
import utime

import stepper

pin = Pin("LED", Pin.OUT)
pin.value()

pin.value(1)
pin.value(0)



ssid = 'NAME OF YOUR WIFI NETWORK'
password = 'YOUR SECRET PASSWORD'


import machine
import time

led= machine.Pin('LED', machine.Pin.OUT)

mot1 = stepper.Steper4([2,3,4,5], 0.002)
while (True):
    led.on()
    #time.sleep(0.001)
    led.off()
    #time.sleep(0.001)
    mot1.doStep(1)