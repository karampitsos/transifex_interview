import aiohttp
import asyncio
import random
from pprint import pprint
import json
from typing import List


class TransifexClient:
    def __init__(self, token: str = '1/8d517de8ea2b8c9a0d872c1e47801c5f33eaa12e'):
        self.token = token
        self.project = 'transifex_interview'
        self.organization = 'karampitsos'
    
    @property
    def headers(self):
        _headers =  {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/vnd.api+json'
        }
        return _headers
    
    async def list_resourcers(self) -> List[str]:
        url = 'https://rest.api.transifex.com/resources'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params = {'filter[project]': f'o:{self.organization}:p:{self.project}'}, headers=self.headers) as response:
                data = await response.json()
                return [d['attributes']['slug'] for d in data['data']]

    async def create_resource(self, name: str):

        json_data = {
            "data": {
                "attributes": {
                "name": name,
                "slug": name,
                },
                "relationships": {
                "i18n_format": {
                    "data": {
                    "id": "KEYVALUEJSON",
                    "type": "i18n_formats"
                    }
                },
                "project": {
                    "data": {
                    "id": f"o:{self.organization}:p:{self.project}",
                    "type": "projects"
                    }
                }
                },
                "type": "resources"
            }
            }
        url = 'https://rest.api.transifex.com/resources'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json_data, headers=self.headers) as response:
                trivia = await response.json()
                return trivia


    async def send_file(self, resource: str, content: str):
        json_data = {
            "data": {
                "attributes": {
                "content": content,
                "content_encoding": "text"
                },
                "relationships": {
                "resource": {
                    "data": {
                    "id": f"o:{self.organization}:p:{self.project}:r:{resource}",
                    "type": "resources"
                    }
                }
                },
                "type": "resource_strings_async_uploads"
            }
            }
        url = 'https://rest.api.transifex.com/resource_strings_async_uploads'
        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.random()*0.5)
            async with session.post(url, json=json_data, headers=self.headers) as response:
                trivia = await response.json()
                return trivia
    
    async def send(self, resource: str, content: str):
        resources = await self.list_resourcers()
        if resource not in resources:
            await self.create_resource(resource)
        await self.send_file(resource, content)

client = TransifexClient()
pprint(asyncio.run(client.send('new', json.dumps({'name': 'osfp'}))))
