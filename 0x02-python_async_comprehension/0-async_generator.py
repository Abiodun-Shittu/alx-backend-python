#!/usr/bin/env python3
"""
Task 0: Write a coroutine called async_generator that takes no arguments.
"""

import asyncio
import random


async def async_generator():
    """
    Generates 10 random numbers asynchronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
