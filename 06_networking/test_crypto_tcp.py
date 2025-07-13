import pytest
import threading
import time
import socket
from crypto_tcp_server import CryptoTCPServer
from crypto_tcp_client import CryptoTCPClient

class TestCryptoTCP:
    
    @pytest.fixture
    def free_port(self):
        """Знаходить вільний порт для тестування."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
    
    @pytest.fixture
    def crypto_server(self, free_port):
        """Створює та запускає CryptoTCPServer."""
        server = CryptoTCPServer('localhost', free_port)
        
        server_thread = threading.Thread(target=server.start)
        server_thread.daemon = True
        server_thread.start()
        
        time.sleep(0.2)
        
        yield server, free_port
        
        try:
            server.stop()
        except:
            pass
    
    def test_crypto_server_creation(self, free_port):
        """Тест створення криптографічного сервера."""
        server = CryptoTCPServer('localhost', free_port)
        
        assert server.host == 'localhost'
        assert server.port == free_port
        assert server.crypto is not None
        assert server.clients == {}
        assert server.clients_lock is not None
    
    def test_crypto_client_creation(self, free_port):
        """Тест створення криптографічного клієнта."""
        client = CryptoTCPClient('localhost', free_port)
        
        assert client.host == 'localhost'
        assert client.port == free_port
        assert client.crypto is not None
        assert client.server_public_key is None
        assert client.is_handshake_done is False
    
    def test_client_server_handshake(self, crypto_server):
        """Тест handshake між клієнтом та сервером."""
        server, port = crypto_server
        
        client = CryptoTCPClient('localhost', port)
        
        try:
            client.connect()
            
            assert client.is_handshake_done is True
            assert client.server_public_key is not None
            
            time.sleep(0.1)  
            connected_clients = server.get_connected_clients()
            assert len(connected_clients) >= 1
            
        finally:
            client.close()
    
    def test_encrypted_echo_communication(self, crypto_server):
        """Тест зашифрованої комунікації echo."""
        server, port = crypto_server
        
        client = CryptoTCPClient('localhost', port)
        
        try:
            client.connect()
            
            test_message = "Hello, encrypted world!"
            response = client.send_encrypted_message(test_message)
            
            expected_response = f"(Echo) {test_message}"
            assert response == expected_response
            
        finally:
            client.close()
    
    def test_multiple_messages(self, crypto_server):
        """Тест відправки кількох повідомлень."""
        server, port = crypto_server
        
        client = CryptoTCPClient('localhost', port)
        
        try:
            client.connect()
            
            messages = ["Message 1", "Message 2", "Повідомлення 3 🔐"]
            
            for msg in messages:
                response = client.send_encrypted_message(msg)
                assert response == f"(Echo) {msg}"
            
        finally:
            client.close()
    
    def test_multiple_clients(self, crypto_server):
        """Тест підключення кількох клієнтів одночасно."""
        server, port = crypto_server
        
        clients = []
        
        try:
            for i in range(3):
                client = CryptoTCPClient('localhost', port)
                client.connect()
                clients.append(client)
            
            time.sleep(0.2)
            connected_clients = server.get_connected_clients()
            assert len(connected_clients) >= 3
            
            for i, client in enumerate(clients):
                message = f"Message from client {i}"
                response = client.send_encrypted_message(message)
                assert response == f"(Echo) {message}"
            
        finally:
            for client in clients:
                try:
                    client.close()
                except:
                    pass
    
    def test_client_without_handshake_fails(self, free_port):
        """Тест що клієнт не може відправляти без handshake."""
        client = CryptoTCPClient('localhost', free_port)
        
        with pytest.raises(Exception) as exc_info:
            client.send_encrypted_message("This should fail")
        
        assert "Handshake not completed" in str(exc_info.value)
    
    def test_client_connection_refused(self):
        """Тест підключення до неіснуючого сервера."""
        client = CryptoTCPClient('localhost', 9999)  
        
        with pytest.raises(ConnectionError):
            client.connect()
    
    def test_unicode_messages(self, crypto_server):
        """Тест з Unicode повідомленнями."""
        server, port = crypto_server
        
        client = CryptoTCPClient('localhost', port)
        
        try:
            client.connect()
            
            unicode_message = "Привіт! 🔐 Test 中文 العربية"
            response = client.send_encrypted_message(unicode_message)
            
            assert response == f"(Echo) {unicode_message}"
            
        finally:
            client.close()