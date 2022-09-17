from typing import List
from category_map import category_map
from clients import TriviaClient, TriviaInput
from parsers import TriviaParser
from transifex_client import TransifexClient
from pipeline import TriviaPipeline
from fastapi import FastAPI
from pydantic import BaseModel
from category_map import category_map
from slugify import slugify

app = FastAPI()

@app.get("/get_categories/")
async def get_categories():
    return category_map

class Items(BaseModel):
    items: List[TriviaInput]

@app.post('/create_resource/')
async def main(items: Items):
    parser = TriviaParser()
    
    transifexclient = TransifexClient(token='1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e',
                                      project='transifex_interview',
                                      organization='karampitsos')
    
    pipelines = [TriviaPipeline().run(
                 consumer = TriviaClient(item),
                 parser = parser,
                 client = transifexclient,
                 resource = slugify(category_map[item.category])
                 )
                 for item in items.items]

    responses = await TriviaPipeline().run_pipelines(pipelines)
    return responses
