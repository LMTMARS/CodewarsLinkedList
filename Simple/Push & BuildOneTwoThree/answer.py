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