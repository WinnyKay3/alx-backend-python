#!/usr/bin/env python3

"""
Safe First Element function.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence if it exists,
    otherwise, return None.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence
        if it exists, otherwise, None.
    """
    if lst:
        return lst[0]
    else:
        return None
