class Node:
    """
    This class represents a node in a linked list.
    """
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

class LinkedList:
    """
    This class represents a linked list.
    """
    def __init__(self, head):
        self.head = Node(head)

    def __str__(self):
        current_node = self.head
        string = ""
        while current_node is not None:
            string += str(current_node.data) + " -> "
            current_node = current_node.next
        string += str(current_node)
        return string

    def append(self, next_data):
        current_node = self.head
        if self.head is None:
            self.head = Node(next_data)
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(next_data)

    def pop(self):
        current_node = self.head
        prev_node = None
        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is not None:
            prev_node.next = None
        else:
            self.head = None
        return current_node.data

    def index(self, value):
        current_node = self.head
        i = 0
        while current_node is not None:
            if current_node.data == value:
                return i
            current_node = current_node.next
            i += 1