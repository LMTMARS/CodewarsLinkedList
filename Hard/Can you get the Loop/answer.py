"""
This code is for Can you get the loop
task.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

def loop_size(node):
    """
    This function determines a
    loop size.
    """
    fast = node
    slow = node
    enc = 0
    while fast and fast.next:
        if fast.next == slow.next:
            enc += 1
            if enc == 2:
                break
        fast = fast.next.next
        slow = slow.next
    res = 0
    while True:
        if fast.next == slow.next:
            enc += 1
            if enc == 4:
                break
        fast = fast.next
        res += 1
    return res