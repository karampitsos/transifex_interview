from pprint import pprint
import asyncio
from trivia_client import TriviaClient
from trivia_parser import TriviaParser
from transifex_client import TransifexClient
from pipeline import TriviaPipeline


async def main():
    client = TriviaClient()
    categories = [10,11,12]
    parser = TriviaParser().parse
    tasks = [TriviaPipeline().run(client.get(category), parser) for category in categories]
    trivias = await asyncio.gather(*tasks)
    return trivias

if __name__ == '__main__':
    pprint(asyncio.run(main()))