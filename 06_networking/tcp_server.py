from tcp_socket import TCPSocket

class TCPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.tcp_socket = TCPSocket(host, port)

    def start(self):
        """Start the TCP server."""
        self.tcp_socket.set_reuse_addr()
        self.tcp_socket.bind()
        self.tcp_socket.listen(5)
        
        while True:
            client_socket = self.tcp_socket.accept()
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
        if self.tcp_socket:
            self.tcp_socket.close()
            print("Server stopped")

if __name__ == "__main__":
    server = TCPServer("localhost", 8081)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()