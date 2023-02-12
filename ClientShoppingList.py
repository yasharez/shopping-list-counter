# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Client file for shopping list counter microservice

# Import libraries
from socket import *
import json

class ClientShoppingList():

  def __init__(self, client_name, client_port, json_list_fp='./shopping-list.json'):
    """
    Initialize client server with user input port & name, load in json list filepath
    """
    self._client_name = client_name
    self._client_port = client_port
    self._json_list_fp = json_list_fp

    json_str = self.load_json_str()

    # Create and bind socket for client
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((self._client_name, self._client_port))

    # Send message to server
    print('Sending-------------------------------------------------')
    clientSocket.sendall(json_str.encode())
    clientSocket.close()

  def load_json_str(self):
    """Load json object into string from filepath"""

    with open(self._json_list_fp, 'r') as f:
      return f.read()


if __name__ == '__main__':
  client = ClientShoppingList('127.0.0.1', 5005)