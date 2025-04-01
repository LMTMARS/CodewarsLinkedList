"""
Code for inserting a node
in a sorted linked list.
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

def sorted_insert(head, data):
    """
    This function inserts
    a node in a right place.
    """
    to_ins = Node(data)

    if head is None or head.data > data:
        to_ins.next = head
        return to_ins
    
    current = head
    while current.next != None and current.next.data < data:
        current = current.next

    to_ins.next = current.next
    current.next = to_ins
    
    return head