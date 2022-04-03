import socket
import threading
import logging


class Server:
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5056
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.connections = []
        self.threads = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

    def handle_client(self, conn, addr):

        print(f"[NEW CONNECTION] {addr} connected.")

        conn.send("Welcome to this chatroom!".encode(self.FORMAT))
        while True:
            try:
                message = conn.recv(2048).decode(self.FORMAT)
                if message:
                    """prints the message and address of the
                    user who just sent the message on the server
                    terminal"""
                    msg = "<user " + str(addr[1]) + "> " + message
                    print(msg)

                    # Calls broadcast function to send message to all

                    self.broadcast(msg.encode(self.FORMAT), conn)

                else:
                    """message may have no content if the connection
                    is broken, in this case we remove the connection"""
                    self.remove(conn)
                    print("[CONNECTION CLOSED] A connection was closed")
                    break

                if "bye" in message or "Bye" in message:
                    self.remove(conn)
                    print("user is left")
                    break
            except:
                continue

    def broadcast(self, message, connection):
        for clients in self.connections:
            if clients != connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    # if the link is broken, we remove the client
                    self.remove(clients)

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            print("[CONNECTION CLOSED] A connection was closed")

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            conn, addr = self.server.accept()
            self.connections.append(conn)
            thread = threading.Thread(
                target=self.handle_client, args=(conn, addr))
            self.threads.append(thread)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
if __name__ == "__main__":
    server = Server()
    server.start()
