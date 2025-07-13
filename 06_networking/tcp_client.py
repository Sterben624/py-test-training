from tcp_socket import TCPSocket

class TCPClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.tcp_socket = TCPSocket(host, port)

    def connect(self):
        """Connect to the TCP server."""
        try:
            self.tcp_socket.connect(self.host, self.port)
        except ConnectionRefusedError:
            raise ConnectionError(f"Cannot connect to server at {self.host}:{self.port}")

    def send_message(self, message):
        """Send a message to the server and receive the echo."""
        if not self.tcp_socket.socket:
            raise Exception("Client is not connected to the server.")
        
        self.tcp_socket.send(message.encode())
        data = self.tcp_socket.receive(1024)
        response = data.decode()
        print(f"Received from server: {response}")
        return response

    def close(self):
        """Close the client socket."""
        if self.tcp_socket.socket:
            self.tcp_socket.close()

if __name__ == "__main__":
    client = TCPClient("localhost", 8081)
    try:
        client.connect()
        while True:
            message = input("Enter message to send to server: ")
            client.send_message(message)
    except KeyboardInterrupt:
        print("\nExiting on user interrupt (Ctrl+C).")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
