import socket
import select
import sys


HEADER = 64
PORT = 5056
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


while(1):
    sockets_list = [sys.stdin, client]
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])
    for socks in read_sockets:
        if socks == client:
            message = socks.recv(2048)
            print(message.decode(FORMAT))
        else:
            message = sys.stdin.readline()
            print("\033[A                             \033[A")
            client.send(message.encode(FORMAT))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
            if "bye" in message or "Bye" in message:
                client.close()
                sys.exit()
