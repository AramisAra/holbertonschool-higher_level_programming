#!/usr/bin/python3
"""4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string
    Args:
        my_str: string to convert
    """
    return json.loads(my_str)
