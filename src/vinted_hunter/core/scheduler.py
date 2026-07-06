import asyncio
from collections.abc import Awaitable, Callable


class Scheduler:
    def __init__(self, interval: int):
        self.interval = interval

    async def start(self, task: Callable[[], Awaitable[None]]) -> None:
        while True:
            await task()
            await asyncio.sleep(self.interval)