#!/usr/bin/python3
"""0. Read file """
def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
