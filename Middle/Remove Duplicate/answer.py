"""
This code is for removing
duplicates from a linked list.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

def remove_duplicates(head):
    """
    This function removes duplicates
    from a linked list.
    """
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
