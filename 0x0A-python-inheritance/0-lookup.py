#!/usr/bin/python3
"""this defines an object attribute lookup function"""


def lookup(obj):
    """this returns a list of an object's available attributes"""
    return (dir(obj))
