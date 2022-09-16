import aiohttp
import asyncio
import random


class TransifexClient:
    def __init__(self, token: str = '1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e'):
        self.token = token
    
    @property
    def headers(self):
        _headers =  {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/vnd.api+json'
        }
        return _headers

    async def create_resource(self):
        json = {}
        url = 'https://rest.api.transifex.com/resources'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json, headers=self.headers) as response:
                trivia = await response.json()
                return trivia


    async def send_file(self):
        url = 'https://rest.api.transifex.com/resource_strings_async_uploads'
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.random()*0.5)
            async with session.post(url, headers=self.headers) as response:
                trivia = await response.json()
                return trivia