#23/01/2024
#Author: Dylan Mwakasekele

import machine, time

red = 15
yellow = 14
green = 13
led = machine.Pin(ledPin, machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)


def 