#!/usr/bin/env python3
"""Import wait_random from the previous python file 
that you’ve written and write an async routine 
called wait_n that takes in 2 int arguments 
(in this order): n and max_delay. You will spawn 
wait_random n times with the specified max_delay.

wait_n should return the list of all the delays 
(float values). The list of the delays should be in 
ascending order without using sort() because of concurrency.
"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """doc"""
    # listDelays = []
    # for _ in range(n):
    #     listDelays.append(asyncio.create_task(wait_random(max_delay)))
    # return sorted(await asyncio.gather(*listDelays))

    # tasks = []
    # delays = []

    # for i in range(n):
    #     task = wait_random(max_delay)
    #     tasks.append(task)

    # for task in asyncio.as_completed((tasks)):
    #     delay = await task
    #     delays.append(delay)

    # return delays
    delays_list = []
    for _ in range(n):
        delays_list.append(asyncio.create_task(wait_random(max_delay)))

    results = await asyncio.gather(*delays_list)
    return sorted(results)
