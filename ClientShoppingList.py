# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Client file for shopping list counter microservice

# Import libraries
from socket import *
import json

class ClientShoppingList():
  """
  Shopping list server class for microservice
  """

  def __init__(self, client_name, client_port, json_list_fp='./shopping-list.json'):
    """
    Initialize client server with user input port & name, load in json list filepath
    """

    self._client_name = client_name
    self._client_port = client_port
    self._json_list_fp = json_list_fp
    self.start_client()

  def start_client(self):
    """
    Start client to send shopping list to server
    """
    json_str = self.get_json_str()

    # Create and bind socket for client
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((self._client_name, self._client_port))

    # Send message to server
    print('Sending-------------------------------------------------')
    clientSocket.sendall(json_str.encode())

    res = clientSocket.recv(1024)
    print(f'Received counts:\n{res.decode()}')



    clientSocket.close()
    
    #self.start_client_server()

  def start_client_server(self):
    """
    Create client server to listen for incoming data
    """

    # Create and bind socket for server
    clientServerSocket = socket(AF_INET, SOCK_STREAM)
    clientServerSocket.bind((self._client_name, self._client_port))
    clientServerSocket.listen(1)
    print(f'Client side server listening on port {self._client_port}...')

    while True:

      # Receive response from server
      connectionSocket, addr = clientServerSocket.accept()
      res = connectionSocket.recv(1024)
      res_len = len(res)

      # Continue receiving information if data is large
      while res_len > 0:
        additional_res = connectionSocket.recv(1024)
        res += additional_res
        res_len = len(additional_res)
      
      print(f'Received counts:\n{res.decode()}')

  def get_json_str(self):
    """Load json object into string from filepath"""

    with open(self._json_list_fp, 'r') as f:
      return f.read()


if __name__ == '__main__':
  client = ClientShoppingList('127.0.0.1', 5005)