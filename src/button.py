#imports
import machine, time

#Set up compinents/global variables
ledPin = 15
led = machine.Pin(ledPin, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Start infinite loop to run program
while True:
    #Main program code
    print(button.value())
    time.sleep(1)