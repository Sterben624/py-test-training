import pytest
import socket
import threading
import time
from tcp_socket import TCPSocket

class TestTCPSocket:
    
    @pytest.fixture
    def free_port(self):
        """Знаходить вільний порт для тестування."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
    
    @pytest.fixture
    def tcp_socket(self, free_port):
        """Створює TCPSocket з вільним портом."""
        sock = TCPSocket('localhost', free_port)
        yield sock
        try:
            sock.close()
        except:
            pass
    
    def test_socket_creation(self, tcp_socket):
        """Тест створення сокета."""
        assert tcp_socket.socket is not None
        assert tcp_socket.host == 'localhost'
        assert tcp_socket.port > 0
    
    def test_bind_socket(self, tcp_socket):
        """Тест прив'язки сокета."""
        tcp_socket.bind()
        bound_address = tcp_socket.socket.getsockname()
        assert bound_address[1] == tcp_socket.port
    
    def test_listen_socket(self, tcp_socket):
        """Тест переведення сокета у режим слухання."""
        tcp_socket.bind()
        tcp_socket.listen(3)
        with pytest.raises(OSError):
            another_socket = socket.socket()
            another_socket.bind(('localhost', tcp_socket.port))
    
    def test_close_socket(self, tcp_socket):
        """Тест закриття сокета."""
        tcp_socket.bind()
        tcp_socket.close()
        test_socket = socket.socket()
        test_socket.bind(('localhost', tcp_socket.port))
        test_socket.close()
    
    def test_client_server_communication(self, free_port):
        """Тест комунікації клієнт-сервер."""
        server_socket = TCPSocket('localhost', free_port)
        client_socket = TCPSocket('localhost', free_port)
        received_data = []
        def server_thread():
            try:
                server_socket.bind()
                server_socket.listen(1)
                client_conn = server_socket.accept()
                data = client_conn.recv(1024)
                received_data.append(data)
                client_conn.sendall(data)
                client_conn.close()
            except Exception as e:
                print(f"Server error: {e}")
        server_thread_obj = threading.Thread(target=server_thread)
        server_thread_obj.daemon = True
        server_thread_obj.start()
        time.sleep(0.1)
        try:
            client_socket.connect('localhost', free_port)
            test_message = b"Hello, TCP!"
            client_socket.send(test_message)
            response = client_socket.receive(1024)
            assert response == test_message
            assert received_data[0] == test_message
        finally:
            client_socket.close()
            server_socket.close()
    
    def test_send_receive_methods(self, free_port):
        """Тест методів send та receive."""
        server_socket = TCPSocket('localhost', free_port)
        client_socket = TCPSocket('localhost', free_port)
        def simple_server():
            server_socket.bind()
            server_socket.listen(1)
            client_conn = server_socket.accept()
            data = server_socket.receive = lambda size: client_conn.recv(size)
            received = server_socket.receive(1024)
            client_conn.sendall(received)
            client_conn.close()
        server_thread = threading.Thread(target=simple_server)
        server_thread.daemon = True
        server_thread.start()
        time.sleep(0.1)
        try:
            client_socket.connect('localhost', free_port)
            test_data = b"Test send/receive"
            client_socket.send(test_data)
            response = client_socket.receive(1024)
            assert response == test_data
        finally:
            client_socket.close()
            server_socket.close()