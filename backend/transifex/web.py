import aiohttp
from typing import Dict


async def post(url, json_data, headers: Dict = {}) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data,
                                headers=headers) as response:
            data = await response.json()
            return data


async def get(url: str, params: Dict, headers: Dict = {}) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params,
                            headers=headers) as response:
            data = await response.json()
            return data
