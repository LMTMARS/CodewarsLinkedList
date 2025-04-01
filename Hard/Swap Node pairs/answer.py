"""
This code is for swapign pairs
in linked lists.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *
    
def swap_pairs(head):
    """
    This function swaps
    nodes in linked list.
    """
    if not head or not head.next:
        return head

    new_head = head.next

    prev = None
    current = head

    while current and current.next:
        next_pair_head = current.next.next
        to_swap = current.next

        to_swap.next = current
        current.next = next_pair_head

        if prev:
            prev.next = to_swap

        prev = current
        current = next_pair_head

    return new_head