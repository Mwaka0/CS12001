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

# Create a socket object​
apSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind it to port 80 (general port)​
apSocket.bind(('', 80))
# Start listening for connections, up to 5​
apSocket.listen(5)
# Print config information​
print(ap.ifconfig())


# Loop to handle all incoming connections (clients)​
while True:
    # Store connection and address details of incoming connection​
    connection, address = apSocket.accept()
    # Print the address of the incoming connection​
    print('Connection by %s' % str(address))
    # store the recieved connection request​
    request = connection.recv(1024)
    # Print the content of the connection request​
    print('Connection Request: %s' % str(request))
    # Send response back to client​    
    connection.send("Hello World")
    # Close the current connection​
    connection.close()