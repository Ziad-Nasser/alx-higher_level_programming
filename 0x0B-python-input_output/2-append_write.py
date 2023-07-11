#!/usr/bin/python3
"""append_file function"""


def append_write(filename="", text=""):
    """append a string at the end of text file and r.n.of char"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
