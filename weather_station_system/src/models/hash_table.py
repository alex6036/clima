# HashTable class for chained hash table
from src.models.linked_list import LinkedList
from src.utils.config import HASH_TABLE_SIZE
import base64

AES_KEY = base64.b64decode("QAREKhIwfWkeZ+Md+o5YWK7nXM9rs/bNZbix7u/YuXk=")
class HashTable:
    def __init__(self):
        self.size = HASH_TABLE_SIZE  # Size of the hash table (prime number)
        self.table = [LinkedList() for _ in range(self.size)]  # Array of linked lists
        self.element_count = 0  # Total number of elements

    def add(self, key, value):
        """Add a key-value pair to the hash table."""
        from src.functions.hash_functions.add import add
        add(self, key, value)

    def remove(self, key):
        """Remove a key-value pair from the hash table."""
        from src.functions.hash_functions.remove_hash import remove_hash
        return remove_hash(self, key)

    def search(self, key):
        """Search for a value by key in the hash table."""
        from src.functions.hash_functions.search_hash import search_hash
        return search_hash(self, key)

    def count_elements(self):
        """Return the total number of elements in the hash table."""
        from src.functions.hash_functions.count_elements import count_elements
        return count_elements(self)