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

    # Setup server info
    serverName, serverPort = '127.0.0.1', 5005

    # Create and bind socket for server
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((self._server_name, self._server_port))
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

      list_counter = ListCounter(req.decode())
      print(list_counter.count_lists())

      connectionSocket.close()

if __name__ == '__main__':
  server = ServerShoppingList('127.0.0.1', 5005)
