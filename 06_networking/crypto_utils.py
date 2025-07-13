from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class CryptoUtils:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
    
    def get_public_key_bytes(self) -> bytes:
        """Серіалізує публічний ключ для передачі по мережі."""
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    def load_public_key_from_bytes(self, key_bytes: bytes):
        """Завантажує публічний ключ з байтів."""
        return serialization.load_pem_public_key(key_bytes)
    
    def encrypt_message(self, message: str, public_key) -> bytes:
        """Шифрує повідомлення публічним ключем."""
        message_bytes = message.encode('utf-8')
        encrypted = public_key.encrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
    
    def decrypt_message(self, encrypted_data: bytes) -> str:
        """Розшифровує повідомлення своїм приватним ключем."""
        decrypted_bytes = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_bytes.decode('utf-8')