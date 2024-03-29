#!/usr/bin/python3
"""this defines a locked class."""


class LockedClass:
    """
    this prevents the user from instantiating new LockedClass
    attributes for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
