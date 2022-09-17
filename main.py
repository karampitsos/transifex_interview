from pprint import pprint
from typing import List
import asyncio
from trivia_client import TriviaClient
from trivia_parser import TriviaParser
from transifex_client import TransifexClient
from pipeline import TriviaPipeline


async def main(categories: List[int]):
    print('run main')
    triviaclient = TriviaClient()
    parser = TriviaParser()
    transifexclient = TransifexClient(token='1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e',
                                      project='transifex_interview',
                                      organization='karampitsos')
    pipelines = [TriviaPipeline().run(consumer = triviaclient.get, parser = parser.parse, client = transifexclient.send, category = category) for category in categories]
    responses = await TriviaPipeline().run_pipelines(pipelines)
    return responses

if __name__ == '__main__':
    pprint(asyncio.run(main([10,11,12])))