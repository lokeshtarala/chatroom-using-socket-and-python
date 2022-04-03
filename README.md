## chatroom-using-socket-and-python
# SOCKET PROGRAMMING:
Sockets can be thought of as endpoints in a communication channel that is bi-directional and establishes communication between a server and one or more clients. Here, we set up a socket on each end and allow a client to interact with other clients via the server. The socket on the server side associates itself with some hardware port on the server side. Any client that has a socket associated with the same port can communicate with the server socket. 

# Multi-Threading:
A thread is a sub-process that runs a set of commands individually from any other thread. So, every time a user connects to the server, a separate thread is created for that user, and communication from the server to the client takes place along individual threads based on socket objects created for the sake of the identity of each client. 
We will require two scripts to establish this chat room. One to keep the serving running, and another that every client should run in order to connect to the server. 

# Server code:
The server is waiting for the clients to request for connection, once the client requests, the request is accepted by the server and the message “Welcome to this chatroom!” is displayed, when a new user comes, a new thread is created for handling his messages, the user's messages are broadcasted with their respective id’s.

# Client code:
Client code sends a request to enter into the chat room for the server, once accepted it can send the message ( input from keyboard ) to the server after every enter press. 
