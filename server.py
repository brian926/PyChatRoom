import threading
import socket
import argparse
import os

class Server(threading.Thread):
    
    def __init__(self, host, port):
        super().__init__()
        self.connections = []
        self.host = host
        self.port = port

    def run(self):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))

        sock.listen(1)
        print('Listening at', sock.getsocketname())

        while True:

            # Accept a new connectino
            sc, sockname = sock.accept()
            print('Accepted a new connection from {} to {}'.format(sc.getpeername(), sc.getsockname()))

            # Create  a new thread
            server_socket = ServerSocket(sc, sockname, self)

            # Start a new thread
            server_socket.start()

            # Add thread to active connection
            self.connections.append(server_socket)
            print('Ready to receive messages from', sc.getpeername())
