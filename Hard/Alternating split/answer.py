"""
This code is for alternating split.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    """
    This function splits a linked list.
    """
    if head is None or head.next is None:
        raise ValueError
    first_head = head
    second_head = head.next
    current_first = first_head
    current_second = second_head
    current = head.next.next
    ind = 2
    while current:
        if ind % 2 == 0:
            current_first.next = current
            current_first = current_first.next
        else:
            current_second.next = current
            current_second = current_second.next

        current = current.next
        ind += 1

    current_first.next = None
    current_second.next = None

    return Context(first_head, second_head)
