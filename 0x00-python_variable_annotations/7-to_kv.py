#!/usr/bin/env python3
"""
String and int/float to tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int/float to a tuple.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square
        of the int/float (as a float).
    """
    return (k, v ** 2.0)
