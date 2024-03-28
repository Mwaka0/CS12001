# Import required Moduals
import network
import time
import socket
import random

#random temperature number
def randomTemp():
    temp = random.randint(-10, 35)
    return temp

#Creating HTML
def creatHTML():
    HTML = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta http-equiv="refresh" content="1">
        <meta charset="UTF-8">
        <title>Temperature</title>
    </head>
    <body>
        <p>This is the current temperature: {temp}</p>
    </body>
    </html>
    """
    return HTML

HTML =""

with open ('webpage.html', 'r') as f:
    HTML = f.read()

# My pico's IP
picoIP = '192.168.4.1'

# Create access point object using 
ap = network.WLAN(network.AP_IF)
# Set up access point configuration (SSID and password)
ap.config(essid="2508934", password="20242023")
# Activate acess point so that it is visible to other devices
ap.active(True)

# Wait until the acess point has finsished activating
while ap.active() == False:
    pass

# Print a message to know that it is active
print('Access Point Activated!')

# Create a socket object
apSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind it to port 80 (general port)
apSocket.bind(("", 80))
# Start listening for connections, up to 5
apSocket.listen(5)
# Print config information
print(ap.ifconfig())

# Loop to handle all incoming connections (clients)
while True:
    # Store connection and address details of incoming connection
    connection, address = apSocket.accept()
   
   # Store the received connection request
    request = connection.recv(1024)
    request = str(request)
    request = request.split()[1]

    # Create temp(temperature) variable 
    temp = randomTemp()
    stringToSend = HTML.format(temp=temp)
    # Send response back to client
    connection.send(stringToSend)
    # Close the current connection
    connection.close()

    