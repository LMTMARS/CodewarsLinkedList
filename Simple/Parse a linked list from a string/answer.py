"""
This code is for Parsing a LL from a string.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ADT import *

def linked_list_from_string(s):
    sep = s.split(' -> ')
    head = None
    for el in sep[-2::-1]:
        head = Node(int(el), head)
    return head
