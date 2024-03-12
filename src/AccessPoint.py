# Import required Moduals
import network
import time
import socket

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

#Create a socket object
apSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind it to port 80 (geral port)
apSocket.bind(('', 80))
# Start listening for connections, up to 5
apSocket.listen(5)