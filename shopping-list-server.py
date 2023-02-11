# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Server file for shopping list counter microservice

# Import libraries
from socket import *
import json

# Setup server info
serverName, serverPort = '127.0.0.1', 5005

# Create and bind socket for server
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print(f'Server listening on port {serverPort}...')

# Start loop for server
while True:

  # Receive request from client
  connectionSocket, addr = serverSocket.accept()
  req = connectionSocket.recv(1024)
  req_len = len(req)

  # Continue receiving information if data is large
  while req_len > 0:
    additional_req = connectionSocket.recv(1024)
    req += additional_req
    req_len = len(additional_req)

  print(req.decode())
  connectionSocket.close()