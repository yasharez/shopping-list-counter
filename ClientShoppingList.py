# Yashar Zafari
# CS 361 - Software Engineering I
# 02/12/2023
# Client file for shopping list counter microservice

# Import libraries
from socket import *
import json

class ClientShoppingList():
  """
  Shopping list server class for microservice
  """

  def __init__(self, server_name, server_port, client_name, client_port, 
                  count_file_name='counts', json_list_fp='./shopping-list.json'):
    """
    Initialize client server with user input port & name, load in json list filepath
    """

    self._server_name = server_name
    self._server_port = server_port
    self._client_name = client_name
    self._client_port = client_port
    self._json_list_fp = json_list_fp
    self._count_file_name = count_file_name + '.json'
    self.start_client()

  def start_client(self):
    """
    Start client to send shopping list to server
    """

    # Load json as string from file
    json_str = self.get_json_str()

    # Create socket for client and connect to server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((self._server_name, self._server_port))

    # Send shopping list to server
    print(f'Sending shopping list file saved at {self._json_list_fp} to counter microservice\n')
    clientSocket.sendall(json_str.encode())
    clientSocket.close()

    # Create a socket and bind to for client side server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.bind((self._client_name, self._client_port))
    clientSocket.listen(1)
    print(f'Client side server listening on port {self._client_port}...\n')

    # Receive response from server
    connectionSocket, addr = clientSocket.accept()
    res = connectionSocket.recv(1024)
    res_len = len(res)

    # Continue receiving information if data is large
    while res_len > 0:
      additional_res = connectionSocket.recv(1024)
      res += additional_res
      res_len = len(additional_res)

    clientSocket.close()
    
    # Notify user that counts have been received and save to file
    print(f'Received shopping list counts from server...\nSaving counts to JSON file "{self._count_file_name}"')
    self.save_counts_file(res.decode())

  def set_count_file_name(self, new_name):
    """Set method for changing counts file name"""

    self._count_file_name = new_name + '.json'

  def get_json_str(self):
    """Load json object into string from filepath"""

    with open(self._json_list_fp, 'r') as f:
      return f.read()

  def save_counts_file(self, json_str):
    """Save a new JSON file with shopping list counts"""

    with open(self._count_file_name, 'w') as f:
      json.dump(json.loads(json_str), f)


if __name__ == '__main__':
  client = ClientShoppingList('127.0.0.1', 5005, '127.0.0.1', 5050, 'counts')