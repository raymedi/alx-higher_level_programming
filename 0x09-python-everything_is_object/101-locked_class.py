#!/usr/bin/python3
"""This define a locked class"""


class LockedClass:
    """
    Only allows installation of an atribute called first_name
    """

    __slots__ = ["first_name"]
