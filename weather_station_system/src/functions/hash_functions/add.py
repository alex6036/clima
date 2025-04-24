# Add function for hash table
from src.functions.hash_functions.hash_function import hash_function
from src.models.node import Node

def add(hash_table, key, value):
    """Add a key-value pair to the hash table."""
    index = hash_function(key)
    # Check if key already exists
    current = hash_table.table[index].head
    while current:
        if current.info[0] == key:
            current.info = (key, value)  # Update value if key exists
            return
        current = current.next
    # Insert new key-value pair
    hash_table.table[index].size += 1
    new_node = Node((key, value))
    new_node.next = hash_table.table[index].head
    hash_table.table[index].head = new_node
    hash_table.element_count += 1