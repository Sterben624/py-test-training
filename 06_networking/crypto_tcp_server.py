from tcp_socket import TCPSocket
from crypto_utils import CryptoUtils
import threading

class CryptoTCPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.tcp_socket = TCPSocket(host, port)
        self.crypto = CryptoUtils()
        
        self.clients = {}
        self.clients_lock = threading.Lock()
    
    def start(self):
        """Запуск сервера."""
        self.tcp_socket.set_reuse_addr()
        self.tcp_socket.bind()
        self.tcp_socket.listen(5)
        print("Crypto server started. Waiting for clients...")
        
        while True:
            client_socket = self.tcp_socket.accept()
            client_thread = threading.Thread(
                target=self.handle_client, 
                args=(client_socket,)
            )
            client_thread.daemon = True
            client_thread.start()
    
    def handle_client(self, client_socket):
        """Обробка клієнта: handshake + повідомлення."""
        try:
            server_public_key = self.crypto.get_public_key_bytes()
            client_socket.sendall(server_public_key)
            
            client_public_key_bytes = client_socket.recv(4096)
            client_public_key = self.crypto.load_public_key_from_bytes(client_public_key_bytes)

            with self.clients_lock:
                self.clients[client_socket] = {
                    'address': client_socket.getpeername(),
                    'public_key': client_public_key
                }
            
            print(f"Handshake completed with {client_socket.getpeername()}")
            
            self.handle_encrypted_messages(client_socket)
            
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            self.disconnect_client(client_socket)

    def handle_encrypted_messages(self, client_socket):
            """Обробка зашифрованих повідомлень від клієнта."""
            while True:
                try:
                    encrypted_data = client_socket.recv(4096)
                    if not encrypted_data:
                        break
                    
                    decrypted_message = self.crypto.decrypt_message(encrypted_data)
                    print(f"Decrypted message from {client_socket.getpeername()}: {decrypted_message}")
                    
                    response = f"(Echo) {decrypted_message}"
                    
                    with self.clients_lock:
                        client_info = self.clients.get(client_socket)
                        if client_info:
                            client_public_key = client_info['public_key']
                            encrypted_response = self.crypto.encrypt_message(response, client_public_key)
                            
                            client_socket.sendall(encrypted_response)
                    
                except Exception as e:
                    print(f"Error processing message from {client_socket.getpeername()}: {e}")
                    break
    
    def disconnect_client(self, client_socket):
        """Відключення клієнта та очищення даних."""
        try:
            with self.clients_lock:
                if client_socket in self.clients:
                    client_info = self.clients.pop(client_socket)
                    print(f"Client {client_info['address']} disconnected")
            
            client_socket.close()
            
        except Exception as e:
            print(f"Error disconnecting client: {e}")
    
    def get_connected_clients(self):
        """Отримати список підключених клієнтів."""
        with self.clients_lock:
            return [info['address'] for info in self.clients.values()]
    
    def stop(self):
        """Зупинка сервера."""
        with self.clients_lock:
            for client_socket in list(self.clients.keys()):
                self.disconnect_client(client_socket)
        
        self.tcp_socket.close()
        print("Crypto server stopped")

if __name__ == "__main__":
    server = CryptoTCPServer("localhost", 8082)
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.stop()