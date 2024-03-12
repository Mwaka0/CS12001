#16/01/2024
#Author: Dylan Mwakasekele

import machine, time

ledPin = 16
led = machine.Pin(ledPin, machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)