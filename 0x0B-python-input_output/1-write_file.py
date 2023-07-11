#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """write a string to text file and r.n.of char"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
