import aiohttp
import asyncio
from typing import Optional, Dict
import random


class TriviaClient:

    url = 'https://opentdb.com/api.php'

    def __init__(self, amount: int = 10, difficulty: Optional[str] = None,
                 type: Optional[str] = None):
        self.amount = amount
        self.difficulty = difficulty
        self.type = type

    @property
    def parameters(self):
        params: Dict = {'amount': self.amount}
        if self.difficulty:
            params['difficulty'] = self.difficulty
        if self.type:
            params['type'] = self.type
        return params

    async def get(self, category: int):
        params = self.parameters.copy()
        params['category'] = category
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.random()*0.5)
            async with session.get(self.url, params=params) as response:
                trivia = await response.json()
                return trivia
