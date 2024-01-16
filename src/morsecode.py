#16/01/2024
#Author: Dylan Mwakasekele

import machine,time

ledPin = "LED"
led = machine.Pin(ledPin, machine.Pin.OUT)

def toggleLEDMorse(type):
    if type == "dash":
        led.toggle()
        time.sleep(1.5)
    elif type == "dot":
        led.toggle()
        time.sleep(0.5)
    else:
        print("Error invalid inuput")
        exit()
    led.toggle()
    time.sleep(0.5) 

#D
toggleLEDMorse("dash")
toggleLEDMorse("dot")
toggleLEDMorse("dot")
#Y
toggleLEDMorse("dash")
toggleLEDMorse("dot")
toggleLEDMorse("dash")
toggleLEDMorse("dash")
#L
toggleLEDMorse("dot")
toggleLEDMorse("dash")
toggleLEDMorse("dot")
toggleLEDMorse("dot")
#A
toggleLEDMorse("dot")
toggleLEDMorse("dash")
#N
toggleLEDMorse("dash")
toggleLEDMorse("dot")

   

