#imports
import machine, time

#Set up compinents/global variables
ledPin = 15
led = machine.Pin(ledPin, machine.Pin.OUT)

#Start infinite loop to run program
while True:
    #Main program code
    led.high()
    time.sleep(0.5)
    led.low()
    time.sleep(0.5)