# Search function for linked lists
def search(lst, key_value, key=lambda x: x):
    current = lst.head
    while current and key(current.info) != key_value:
        current = current.next
    return current.info if current else None