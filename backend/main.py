from typing import List, Union
from category_map import category_map
from trivia_client import TriviaClient
from trivia_parser import TriviaParser
from transifex_client import TransifexClient
from pipeline import TriviaPipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/get_categories/")
async def get_categories():
    return category_map

class Item(BaseModel):
    categories: List[int]
    amount: Union[str, None] = None
    difficulty: Union[str, None] = None
    type: Union[str, None] = None

@app.post('/create_resource/')
async def main(item: Item):
    triviaclient = TriviaClient()
    parser = TriviaParser()
    transifexclient = TransifexClient(token='1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e',
                                      project='transifex_interview',
                                      organization='karampitsos')
    pipelines = [TriviaPipeline().run(consumer = triviaclient.get, parser = parser.parse, client = transifexclient.send, category = category) for category in item.categories]
    responses = await TriviaPipeline().run_pipelines(pipelines)
    return responses
