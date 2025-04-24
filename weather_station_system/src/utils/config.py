# Configuration file for system parameters
# Configuration file for system parameters
import base64

# AES key (256 bits, encoded in base64 for safety)
# Generated with: import os; print(base64.b64encode(os.urandom(32)).decode('utf-8'))
AES_KEY = base64.b64decode("YOUR_SECURE_KEY_HERE")  # Replace with a secure key

# Hash table size (prime number to minimize collisions)
HASH_TABLE_SIZE = 29