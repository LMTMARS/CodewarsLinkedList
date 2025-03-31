import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

def push(head, data):
    """
    This function pushes a node.
    """
    return Node(data, head)

def build_one_two_three():
    """
    This function builds one two three.
    """
    head = None
    for i in range(3,0, -1):
        head = push(head, i)
    return head


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    """
    This function moves Node
    """
    if source is None or (source is None and dest is None):
        raise ValueError
    
    source_upd = source.next
    dest_upd = push(dest, source.data)
    
    return Context(source_upd, dest_upd)


def print_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" -> ".join(result) + " -> None")

# Example usage
source = Node(1, Node(2, Node(3)))
dest = Node(4, Node(5, Node(6)))

result = move_node(source, dest)
print("Source after move:")
print_list(result.source)
print("Destination after move:")
print_list(result.dest)