# Yashar Zafari
# CS 361 - Software Engineering I
# 02/11/2023
# Server file for shopping list counter microservice

# Import libraries
from socket import *
from ListCounter import *

class ServerShoppingList:
  """
  Shopping list server class for microservice
  """

  def __init__(self, server_name, server_port):
    """
    Initialize server with inputted server name and port values
    """

    self._server_name = server_name
    self._server_port = server_port
    self.start_server()

  def start_server(self):
    """
    Start server to listen for incoming shopping lists
    """

    # Create and bind socket for server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((self._server_name, self._server_port))
    serverSocket.listen(1)
    print(f'Server listening on port {self._server_port}...')

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

      list_counter = ListCounter(req.decode())

      connectionSocket.send(list_counter.count_lists().encode())
      print(list_counter.count_lists())

      connectionSocket.close()

if __name__ == '__main__':
  server = ServerShoppingList('127.0.0.1', 5005)
