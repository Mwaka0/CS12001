#23/01/2024
#Author: Dylan Mwakasekele

import machine, time

red = 15
yellow = 14
green = 13

while True:
    toggleLED(red)
    time.sleep(0.5)


def toggleLED(colour):
    led = machine.Pin(ledPin, machine.Pin.OUT)
    led.toggle()