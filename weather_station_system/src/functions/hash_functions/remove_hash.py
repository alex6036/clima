# Remove_hash function for hash table
from src.functions.hash_functions.hash_function import hash_function

def remove_hash(hash_table, key):
    """Remove a key-value pair from the hash table."""
    index = hash_function(key)
    current = hash_table.table[index].head
    if not current:
        return None
    # Check if the first node has the key
    if current.info[0] == key:
        hash_table.table[index].head = current.next
        hash_table.table[index].size -= 1
        hash_table.element_count -= 1
        return current.info[1]
    # Search for the key
    while current.next and current.next.info[0] != key:
        current = current.next
    if current.next:
        removed_value = current.next.info[1]
        current.next = current.next.next
        hash_table.table[index].size -= 1
        hash_table.element_count -= 1
        return removed_value
    return None