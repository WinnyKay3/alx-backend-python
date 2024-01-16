#!/usr/bin/env python3
"""
Module with a function to create asyncio.Tasks for task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for task_wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
