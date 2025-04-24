# Hash function for hash table
from src.utils.config import HASH_TABLE_SIZE

def hash_function(key):
    """Compute the hash index for a given key."""
    if not isinstance(key, str):
        key = str(key)
    # Sum ASCII values of characters and apply modulo
    hash_value = sum(ord(c) for c in key)
    return hash_value % HASH_TABLE_SIZE