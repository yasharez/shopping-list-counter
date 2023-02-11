# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Client file for shopping list counter microservice

# Import libraries
from socket import *
import json

# Create variable for shopping list file name
shopping_list_json_file = './shopping-list.json'

# Load in json file and convert to string
with open(shopping_list_json_file, 'r') as f:
  json_str = f.read()

# Setup server info
serverName, serverPort = '127.0.0.1', 5005

# Create and bind socket for client
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Send message to server
print('Sending-------------------------------------------------')
clientSocket.sendall(json_str.encode())
clientSocket.close()