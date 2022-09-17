from __future__ import annotations
from typing import Awaitable, List
import asyncio
from clients import Client
from parsers import Parser
from transifex_client import TransifexClient


class TriviaPipeline:

    async def run(self, consumer: Client, parser: Parser, client: TransifexClient, resource: str):
        data = await consumer.get()
        print(data)
        parsed = parser.parse(data)
        print(parsed)
        response = await client.send(resource, parsed)
        return response
    
    @classmethod
    async def run_pipelines(cls, pipelines: List[Awaitable]):
        results = await asyncio.gather(*pipelines)
        return results
