# Remove function for linked lists
def remove(lst, key_value, key=lambda x: x):
    if not lst.head:
        return None

    if key(lst.head.info) == key_value:
        removed = lst.head.info
        lst.head = lst.head.next
        lst.size -= 1
        return removed

    current = lst.head
    while current.next and key(current.next.info) != key_value:
        current = current.next

    if current.next:
        removed = current.next.info
        current.next = current.next.next
        lst.size -= 1
        return removed
    return None