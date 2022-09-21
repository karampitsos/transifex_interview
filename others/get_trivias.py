from pprint import pprint
import asyncio
from transifex.clients import TriviaClient, TriviaInput

async def main():
    client = TriviaClient(data=TriviaInput(category = 12, amount = 5))
    data = await client.get()
    return data

if __name__ == '__main__':

    data = asyncio.run(main())
    pprint(data)