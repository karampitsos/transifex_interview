import aiohttp
import asyncio
from typing import Optional, Dict, Optional
import random
from clients import Client
from pydantic import BaseModel


class TriviaInput(BaseModel):
    category: int
    amount: int = 10
    difficulty: Optional[str]
    type: Optional[str]


class TriviaClient(Client):

    url = 'https://opentdb.com/api.php'

    def __init__(self, data: TriviaInput):
        self.data = data

    async def get(self) -> Dict:
        print(f'run trivia client: {self.data.category}')
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.random()*0.5)
            async with session.get(self.url, params=self.data.dict(exclude_none=True)) as response:
                trivia = await response.json()
                return trivia
