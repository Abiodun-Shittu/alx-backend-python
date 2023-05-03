#!/usr/bin/env python3
"""
Task 1: write an async routine called wait_n that takes in 2 int arguments
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait for.

    Returns:
        List[float]: List of all the delays in ascending order.
    '''
    # create a list to store all the tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]

    # wait for all tasks to complete and gather their results
    delays = await asyncio.gather(*tasks)

    # return the list of delays sorted in ascending order
    return sorted(delays)
