import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *


def get_nth(node, index):
    """
    This function gets an
    nth node.
    """
    current = node
    count = index
    if index < 0:
        raise IndexError
    while count > 0:
        if current.next is None:
            raise IndexError
        current = current.next
        count -= 1
    return current