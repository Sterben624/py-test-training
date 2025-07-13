import socket

class TCPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        """Start the TCP server."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # дозволяє перевикористання порту
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)  # 50 занадто багато для простого тесту
        print(f"Server started on {self.host}:{self.port}")
        
        while True:  # основний цикл сервера
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address}")
            self.handle_client_echo(client_socket)

    def handle_client_echo(self, client_socket):
        """Handle client connection and echo messages."""
        with client_socket:
            print("Client connected")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                client_socket.sendall(data)

    def stop(self):
        """Stop the TCP server."""
        if self.server_socket:
            self.server_socket.close()
            print("Server stopped")

if __name__ == "__main__":
    server = TCPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()