import aiohttp
import asyncio
from typing import Optional, Dict, Optional
import random
from client import Client
from pydantic import BaseModel

class TriviaInput(BaseModel):
    category: int
    amount: int
    difficulty: Optional[str]
    type: Optional[str]


class TriviaClient(Client):

    url = 'https://opentdb.com/api.php'

    def __init__(self, category: int, amount: int = 10, difficulty: Optional[str] = None,
                 type: Optional[str] = None):
        self.category = category
        self.amount = amount
        self.difficulty = difficulty
        self.type = type

    @property
    def parameters(self):
        params: Dict = {'category': self.category, 'amount': self.amount}
        if self.difficulty:
            params['difficulty'] = self.difficulty
        if self.type:
            params['type'] = self.type
        return params

    async def get(self) -> Dict:
        print(f'run trivia client: {self.category}')
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.random()*0.5)
            async with session.get(self.url, params=self.parameters) as response:
                trivia = await response.json()
                return trivia
