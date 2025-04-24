# Insert function for linked lists
def insert(lst, element, key=lambda x: x):
    from src.models.node import Node
    new_node = Node(element)
    lst.size += 1

    if not lst.head or key(element) < key(lst.head.info):
        new_node.next = lst.head
        lst.head = new_node
        return

    current = lst.head
    while current.next and key(current.next.info) < key(element):
        current = current.next

    new_node.next = current.next
    current.next = new_node