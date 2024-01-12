#!/usr/bin/env python3

"""
Element length function.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains a sequence
        from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
