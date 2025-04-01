"""
This code is for Recursive reverse.
"""
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

def reverse(head):
    """
    This function reverse a LinkedList
    """
    if head is not None and head.next is not None:
        
        new = reverse(head.next)

        head.next.next = head
        head.next = None
        return new
    return head