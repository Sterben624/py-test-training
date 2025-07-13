from tcp_socket import TCPSocket
from crypto_utils import CryptoUtils

class CryptoTCPClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.tcp_socket = TCPSocket(host, port)
        self.crypto = CryptoUtils()
        self.server_public_key = None
        self.is_handshake_done = False
    
    def connect(self):
        """Підключення до сервера."""
        try:
            self.tcp_socket.connect(self.host, self.port)
            print(f"Connected to crypto server at {self.host}:{self.port}")
            
            self.perform_handshake()
            
        except ConnectionRefusedError:
            raise ConnectionError(f"Cannot connect to crypto server at {self.host}:{self.port}")
    
    def perform_handshake(self):
        """Обмін публічними ключами з сервером."""
        try:
            server_public_key_bytes = self.tcp_socket.receive(4096)
            self.server_public_key = self.crypto.load_public_key_from_bytes(server_public_key_bytes)
            print("Received server's public key")
            
            client_public_key_bytes = self.crypto.get_public_key_bytes()
            self.tcp_socket.send(client_public_key_bytes)
            print("Sent client's public key")
            
            self.is_handshake_done = True
            print("Handshake completed successfully!")
            
        except Exception as e:
            raise Exception(f"Handshake failed: {e}")
    
    def send_encrypted_message(self, message: str) -> str:
        """Відправка зашифрованого повідомлення та отримання відповіді."""
        if not self.is_handshake_done:
            raise Exception("Handshake not completed. Cannot send encrypted messages.")
        
        if not self.server_public_key:
            raise Exception("Server's public key not available.")
        
        try:
            encrypted_message = self.crypto.encrypt_message(message, self.server_public_key)
            print(f"Sending encrypted message: {message}")
            
            self.tcp_socket.send(encrypted_message)
            
            encrypted_response = self.tcp_socket.receive(4096)
            
            decrypted_response = self.crypto.decrypt_message(encrypted_response)
            print(f"Received decrypted response: {decrypted_response}")
            
            return decrypted_response
            
        except Exception as e:
            raise Exception(f"Error sending encrypted message: {e}")
    
    def close(self):
        """Закриття з'єднання."""
        if self.tcp_socket.socket:
            self.tcp_socket.close()
            self.is_handshake_done = False
            self.server_public_key = None
            print("Crypto client connection closed")

if __name__ == "__main__":
    client = CryptoTCPClient("localhost", 8082)
    try:
        client.connect()
        
        while True:
            message = input("Enter message to encrypt and send: ")
            if message.lower() == 'quit':
                break
                
            response = client.send_encrypted_message(message)
            print(f"Server response: {response}")
            
    except KeyboardInterrupt:
        print("\nExiting on user interrupt (Ctrl+C).")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()