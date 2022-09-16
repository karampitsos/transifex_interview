from typing import Awaitable


class TriviaPipeline:

    async def run(self, consumer: Awaitable, parser):
        data = await consumer
        return parser(data)