#!/usr/bin/env python3
"""
Module with a function to create an asyncio.Task for wait_random.
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
