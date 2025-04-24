# Search_hash function for hash table
from src.functions.hash_functions.hash_function import hash_function

def search_hash(hash_table, key):
    """Search for a value by key in the hash table."""
    index = hash_function(key)
    current = hash_table.table[index].head
    while current:
        if current.info[0] == key:
            return current.info[1]
        current = current.next
    return None