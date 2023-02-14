# shopping-list-counter
CS361 Microservice to receive JSON file and return count for each shopping list within file

Created by: Yashar Zafari

Communication Contract:

To first set up the microservice, the client and server will need to create an instance of ClientShoppingList and ServerShoppingList respectively. Both classes are initialized with a server IP address, server port number, client IP address, and client port number. The ClientShoppingList also takes two optional parameters: a filename to save the shopping list counts to, and a filepath to where the shopping list JSON file is stored on the local system. If no user value is inputted then they will default to 'counts.json' and './shopping-list.json' respectively. Lastly, the server should have the ListCounter.py file in the local directory as it is used in the ServerShoppingList class.

1. Requesting Data: To request data, the client should have a JSON file of shopping list items saved in a local directory and pass the filepath to the ClientShoppingList object through the init method, or using ClientShoppingList.set_filepath([filepath value]). Once the filepath is correctly set, the user can then use the ClientShoppingList.start_client() method to connect to the server IP address and port number and send the JSON file to the server.

2. Receving Data: The ClientShoppingList.start_client() is set up in a way such that it automatically receives the count of shopping list items from the server once the calculation is done. The client does not need to make any additional requests to the server to receive the data.

3. UML Sequence Diagram:![CS361 Microservice UML](https://user-images.githubusercontent.com/70769454/218605491-40de4b5e-4746-4378-9ce3-cf064ad2e5ca.png)
