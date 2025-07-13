import pytest
from crypto_utils import CryptoUtils

class TestCryptoUtils:
    
    @pytest.fixture
    def crypto_instance(self):
        return CryptoUtils()
    
    def test_key_generation(self, crypto_instance):
        assert crypto_instance.private_key is not None
        assert crypto_instance.public_key is not None
    
    def test_public_key_serialization(self, crypto_instance):
        key_bytes = crypto_instance.get_public_key_bytes()
        
        assert isinstance(key_bytes, bytes)
        assert len(key_bytes) > 0
        assert b'BEGIN PUBLIC KEY' in key_bytes
    
    def test_public_key_loading(self, crypto_instance):
        key_bytes = crypto_instance.get_public_key_bytes()
        
        loaded_key = crypto_instance.load_public_key_from_bytes(key_bytes)
        
        assert loaded_key is not None
        assert loaded_key.public_numbers() == crypto_instance.public_key.public_numbers()
    
    def test_encrypt_decrypt_message(self, crypto_instance):
        message = "Hello, encrypted world!"
        
        encrypted = crypto_instance.encrypt_message(message, crypto_instance.public_key)
        
        assert isinstance(encrypted, bytes)
        assert len(encrypted) > 0
        assert encrypted != message.encode()
        
        decrypted = crypto_instance.decrypt_message(encrypted)
        
        assert decrypted == message
    
    def test_encrypt_decrypt_unicode(self, crypto_instance):
        message = "Привіт! 😁 Test 123"
        
        encrypted = crypto_instance.encrypt_message(message, crypto_instance.public_key)
        decrypted = crypto_instance.decrypt_message(encrypted)
        
        assert decrypted == message