# Yashar Zafari
# CS 361 - Software Engineering I
# 02/12/2023
# Server file for shopping list counter microservice

# Import libraries
from socket import *
from ListCounter import *
import json

class ServerShoppingList:
  """
  Shopping list server class for microservice
  """

  def __init__(self, server_name, server_port, client_name, client_port):
    """
    Initialize server with inputted server name and port values
    """

    self._server_name = server_name
    self._server_port = server_port
    self._client_name = client_name
    self._client_port = client_port
    self._counts_json = {}
    self.start_server()

  def start_server(self):
    """
    Start server to listen for incoming shopping lists
    """

    # Create and bind socket for server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((self._server_name, self._server_port))
    serverSocket.listen(1)
    print(f'Server listening on port {self._server_port}...\n')

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

      # Create ListCount object to count items in json list
      list_counter = ListCounter(req.decode())
      self._counts_json = list_counter.count_lists()
      self.send_counts_to_client()
      connectionSocket.close()

  def send_counts_to_client(self):
    """
    Send counts JSON to client
    """

    # Convert JSON to string
    counts_str = json.dumps(self._counts_json)

    # Create and bind socket to client
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((self._client_name, self._client_port))

    # Send counts to client
    print('Sending shopping list counts to client...')
    clientSocket.sendall(counts_str.encode())
    clientSocket.close()

if __name__ == '__main__':
  server = ServerShoppingList('127.0.0.1', 5005, '127.0.0.1', 5050)
