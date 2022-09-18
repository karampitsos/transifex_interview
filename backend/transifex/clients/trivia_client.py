from transifex import web
from typing import Optional, Dict
from transifex.clients import Client
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
    
    @property
    def params(self):
        return self.data.dict(exclude_none=True)

    async def get(self) -> Dict:
        trivias = await web.get(self.url, self.params)
        return trivias
