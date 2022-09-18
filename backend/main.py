from typing import List
from transifex.clients.trivia_client import category_map
from transifex.clients import TriviaClient, TriviaInput
from transifex.parsers import TriviaParser
from transifex import TransifexClient
from transifex import Pipeline
from fastapi import FastAPI
from pydantic import BaseModel
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

    transifexclient = TransifexClient(
                        token='1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e',
                        project='transifex_interview',
                        organization='karampitsos')

    pipelines = [Pipeline().run(
                 consumer=TriviaClient(item),
                 parser=parser,
                 client=transifexclient,
                 resource=slugify(category_map[item.category])
                 )
                 for item in items.items]

    responses = await Pipeline().run_pipelines(pipelines)
    return responses
