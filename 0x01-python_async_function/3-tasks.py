#!/usr/bin/env python3
"""
Task 3: Write a function (do not create an async function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task that waits for a random delay between 0 and
    max_delay seconds.
    """
    return asyncio.create_task(wait_random(max_delay))
