#!/usr/bin/env python3
"""
Safely Get Value function.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
  -> Union[Any, T]:
    """
    Get the value from a dictionary safely.
    If the key is present, return the corresponding value;
    otherwise, return the default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value
        to return if the key is not present. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key if it exists,
        otherwise, the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
