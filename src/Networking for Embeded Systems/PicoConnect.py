# Import required moduals
import network
import time 
import socket
import machine



# Set up config values
SSID = ""
password = ""

def connectToPico(SSID, password):
    b = 1


def closeConnectionToPico(socket):
    return False

def requestData(socket):
    a = 1

# Create a WLAN object
wlan = network.WLAN(network.STA_IF)
# Activate wireless communicatioin
wlan.active(True)
# Connect to the access point of another pico
wlan.connect(SSID, password)

# Wait until fully connected
while wlan.isconnected() == False:
    print('Waiting for connection...')
    time.sleep(1)

# Print the config 
print(wlan.ifconfig())
#IP of the AP pico
ip = ""

while True:
    server = socket.getaddrinfo(ip, 80)
    # Address of Web Server
    address = server[0][-1]
    # Create a scoket 
    serverSocket = socket.socket()
    # Open socket connection with server
    serverSocket.connect(address)
    # Send rewuest to server to get data
    serverSocket.send(b"GET /data")

    # Store response from server
    response=str(serverSocket.recv(512))

    print(response)

    # Close socket
    serverSocket.close()

    time.sleep(0.2)