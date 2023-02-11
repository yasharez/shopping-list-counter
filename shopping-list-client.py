# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Client file for shopping list counter microservice

# Import libraries
from socket import *
import json

# Setup server info
serverName, serverPort = '127.0.0.1', 5005

# Create and bind socket for client
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Send message to server
print('Sending-------------------------------------------------')
req = 10000000 * 'a'
clientSocket.sendall(req.encode())
clientSocket.close()