#!/usr/bin/env python3
"""
Make multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that takes
        a float and returns the result of multiplication.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiply a float by the given multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier

    return multiplier_function
