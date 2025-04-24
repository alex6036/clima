# Decrypt function for AES decryption
from Crypto.Cipher import AES
from src.utils.config import AES_KEY
import base64

def decrypt(encrypted_data):
    """Decrypt a string using AES-256."""
    # Decode from base64
    encrypted_data = base64.b64decode(encrypted_data)
    
    # Extract nonce, tag, and ciphertext
    nonce = encrypted_data[:16]  # EAX nonce is 16 bytes
    tag = encrypted_data[16:32]  # Tag is 16 bytes
    ciphertext = encrypted_data[32:]
    
    # Create cipher object
    cipher = AES.new(AES_KEY, AES.MODE_EAX, nonce=nonce)
    
    # Decrypt and verify
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode('utf-8')