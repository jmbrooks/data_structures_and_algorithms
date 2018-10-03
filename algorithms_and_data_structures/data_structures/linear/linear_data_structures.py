# -*- coding: utf-8 -*-


class Stack():
"""Implements Stack abstract linear data structure."""
def __init__(self):
    self.items = []

def is_empty(self):
    return self.items == []

def size(self):
    return len(self.items)

def pop(self):
    self.items.pop()

def peek(self):
    return self.items[-1]

def push(self, item):
    self.items.append(item)
