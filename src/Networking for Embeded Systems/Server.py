import network
import time
import socket
from machine import Pin
import random
 
def randomTemp():
    temp = random.randint(-10, 35)
    return temp
 
html_string = ""
 
with open('page.html', 'r') as f:
    html_string = f.read()
 
ap = network.WLAN(network.AP_IF)
ap.config(essid='NAME', password='PASSWORD')
ap.active(True)
 
while not ap.active():
    pass
 
print('AP Mode Is Active, You can Now Connect')
# print('SSID:', ap.config("essid"))
# print('IP Address To Connect to:', ap.ifconfig()[0])
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print(ap.ifconfig())
 
temperature = 0
dustparticles = 0
 
 
while True:
 
    connection, address = s.accept()
    print("connection established from %s" % str(address))
    request = connection.recv(1024)
    request = request.decode()
   
    print("connection request from %s" % str(address))
 
    if '/FROMPICO' in request:
        data = request.split(":")
        temperature = data[1]
        dustparticles = data[2]
        print(temperature)
        print(dustparticles)
    
    stringToSend = html_string
    stringToSend = stringToSend.replace("{ temp }", str(temperature))
    stringToSend = stringToSend.replace("{ dustP }", str(dustparticles))

    connection.send(stringToSend)
    connection.close()