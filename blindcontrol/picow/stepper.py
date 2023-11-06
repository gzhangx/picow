from machine import Pin
import utime

# https://learn.adafruit.com/assets/99339  4,5,6,7
# https://www.youngwonks.com/blog/How-to-use-a-stepper-motor-with-the-Raspberry-Pi-Pico
def mapPins(pin):
    return Pin(pin, Pin.OUT)
    
class Steper4(object):
    def __init__(self, pins, delay = 0.001):
        print('test1')
        self.pins = list(map(mapPins,pins))
        print(pins)
        print(self.pins)
        self.stepSequence = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
        self.delay = delay
        
        
    def doStep(self):        
        #ddf = (lambda a:a) if dir>0 else reversed;
        for step in self.stepSequence:
            for i in reversed(range(len(self.pins))):
                self.pins[i].value(step[i])
                utime.sleep(self.delay)