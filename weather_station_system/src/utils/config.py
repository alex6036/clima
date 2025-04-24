# Configuration file for system parameters
import base64

# AES key (256 bits, encoded in base64 for safety)
AES_KEY = base64.b64decode("qX7p9z2k8L4mN6oPqRsTuVwXyZ0aBcDeFgHiJkLmNoP=")  # Reemplaza con tu clave generada

# Hash table size (prime number to minimize collisions)
HASH_TABLE_SIZE = 29