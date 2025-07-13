import socket

class TCPSocket:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self):
        """Bind the socket to the host and port."""
        self.socket.bind((self.host, self.port))
        print(f"Socket bound to {self.host}:{self.port}")

    def listen(self, backlog=5):
        """Listen for incoming connections."""
        self.socket.listen(backlog)
        print(f"Socket listening on {self.host}:{self.port} with backlog {backlog}")

    def accept(self):
        """Accept a connection from a client."""
        client_socket, address = self.socket.accept()
        print(f"Connection accepted from {address}")
        return client_socket
    
    def connect(self, host, port):
        self.socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

    def send(self, data: bytes):
        self.socket.sendall(data)

    def receive(self, size=1024) -> bytes:
        return self.socket.recv(size)
    
    def close(self):
        """Close the socket."""
        self.socket.close()
        print("Socket closed")