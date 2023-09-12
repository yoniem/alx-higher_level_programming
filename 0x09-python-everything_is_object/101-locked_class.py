#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevents the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    _slots_ = ["first_name"]
