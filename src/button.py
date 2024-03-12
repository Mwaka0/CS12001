#imports
import machine, time

#Set up compinents/global variables
ledPin = 16
led = machine.Pin(ledPin, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Start infinite loop to run program
while True:
    #Main program code
    if button.value(): 
        led.high()
    else:
        led.low()