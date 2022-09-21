from transifex import web
from typing import Optional, Dict, List, Tuple
from transifex.clients import Client
from pydantic import BaseModel
import requests
import json


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
    def params(self) -> Dict:
        return self.data.dict(exclude_none=True)

    async def get(self) -> Dict:
        trivias = await web.get(self.url, self.params)
        return trivias


category_map = {
    0:  'Entertainment: Comics',
    9:  'General Knowledge',
    10: 'Entertainment: Books',
    11: 'Entertainment: Film',
    12: 'Entertainment: Music',
    13: 'Entertainment: Musicals & Theatres',
    14: 'Entertainment: Television',
    15: 'Entertainment: Video Games',
    16: 'Entertainment: Board Games',
    17: 'Science & Nature',
    18: 'Science: Computers',
    19: 'Science: Mathematics',
    20: 'Mythology',
    21: 'Sports',
    22: 'Geography',
    23: 'History',
    24: 'Politics',
    25: 'Art',
    26: 'Celebrities',
    27: 'Animals',
    28: 'Vehicles',
    29: 'Entertainment: Comics',
    30: 'Science: Gadgets',
    31: 'Entertainment: Japanese Anime & Manga',
    32: 'Entertainment: Cartoon & Animations'
}


def collect_categories(trials: List[int]) -> List[Tuple(int, str)]:

    categories: List[str] = []
    for trial in trials:
        url = f'https://opentdb.com/api.php?amount=1&category={trial}'
        response = requests.get(url)
        try:
            categories.append(
                (trial, json.loads(response.text)['results'][0]['category'])
                )
        except requests.exceptions.RequestException:
            print(f'None category for {trial}')

    return categories
