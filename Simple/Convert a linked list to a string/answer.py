"""
This code is for converting a linked list to a string task.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

def stringify(head_node):
    """
    This function transforms
    a linked list into a string.
    """
    res = ''
    current = head_node
    while current:
        res += f'{current.data} -> '
        current = current.next
    return res + 'None'