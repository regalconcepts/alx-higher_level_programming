#!/usr/bin/python3
"""this defines an inherited list class MyList"""


class MyList(list):
    """this implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """this prints a list in sorted ascending order"""
        print(sorted(self))
