# Encrypt function for AES encryption
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from src.utils.config import AES_KEY
import base64

def encrypt(data):
    """Encrypt a string using AES-256."""
    # Ensure data is bytes
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Create cipher object
    cipher = AES.new(AES_KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    
    # Encrypt data
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    # Combine nonce, tag, and ciphertext
    encrypted_data = nonce + tag + ciphertext
    return base64.b64encode(encrypted_data).decode('utf-8')