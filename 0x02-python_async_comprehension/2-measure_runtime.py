#!/usr/bin/env python3
"""Import async_comprehension from the
previous file and write a measure_runtime
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total
runtime and return it.

Notice that the total runtime is roughly
10 seconds, explain it to yourself.
"""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Return the total runtime of an async_comprehension
    func execution of 4 times in parallel.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
