from __future__ import annotations
from typing import Awaitable, List
import asyncio
from category_map import category_map
from slugify import slugify


class TriviaPipeline:

    async def run(self, consumer: Awaitable, parser: Awaitable, client: Awaitable, category: int):
        print( f'run pipeline: {category}')
        data = await consumer(category)
        parsed = parser(data)
        response = await client(slugify(category_map[category]), parsed)
        return response
    
    @classmethod
    async def run_pipelines(cls, pipelines: List[Awaitable]):
        results = await asyncio.gather(*pipelines)
        return results
