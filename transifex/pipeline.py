from __future__ import annotations
from typing import Awaitable, List, Dict
import asyncio
from transifex.clients import Client
from transifex.parsers import Parser
from transifex.transifex_client import TransifexClient


class Pipeline:

    async def run(self, consumer: Client, parser: Parser,
                  client: TransifexClient, resource: str) -> Dict:
        data = await consumer.get()
        parsed = parser.parse(data)
        response = await client.send(resource, parsed)
        return response

    @classmethod
    async def run_pipelines(cls, pipelines: List[Awaitable]) -> List[Dict]:
        results = await asyncio.gather(*pipelines)
        return results
