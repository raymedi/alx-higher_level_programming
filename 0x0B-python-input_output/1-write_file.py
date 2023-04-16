#!/usr/bin/python3
"""
functions written and returned the characters written.
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
