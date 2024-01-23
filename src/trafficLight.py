#23/01/2024
#Author: Dylan Mwakasekele

import machine, time

red = 15
yellow = 14
green = 13

def toggleLED(ledPin):
    led = machine.Pin(ledPin, machine.Pin.OUT)
    led.toggle()

while True:
    toggleLED(red)
    time.sleep(0.75)
    toggleLED(yellow)
    time.sleep(0.75)
    toggleLED(red)
    toggleLED(yellow)
    toggleLED(green)
    time.sleep(0.75)
    toggleLED(green)
    toggleLED(yellow)
    time.sleep(0.75)
    toggleLED(yellow)
