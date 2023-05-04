#!/usr/bin/env python3
"""
Task 1: write a coroutine called async_comprehension that takes no arguments.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over
    async_generator and returns the 10 random numbers.
    """
    return [x async for x in async_generator()]
