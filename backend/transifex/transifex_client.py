from typing import List, Dict
import json
from transifex import web


class TransifexClient:
    def __init__(self, token: str, project: str, organization: str):
        self.token = token
        self.project = project
        self.organization = organization

    @property
    def headers(self):
        _headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/vnd.api+json'
        }
        return _headers

    async def list_resources(self) -> List[str]:
        url = 'https://rest.api.transifex.com/resources'
        params = {'filter[project]': f'o:{self.organization}:p:{self.project}'}
        data = await web.get(url, params, self.headers)
        return [d['attributes']['slug'] for d in data['data']]

    async def list_strings(self, resource: str) -> Dict:
        url = 'https://rest.api.transifex.com/resource_strings'
        params = {'filter[resource]':f"o:{self.organization}:p:{self.project}:r:{resource}"}
        data = await web.get(url, params, self.headers)
        output = { d['attributes']['key']: d['attributes']['strings']['other'] for d in data['data']}
        return output

    async def create_resource(self, name: str) -> Dict:
        url = 'https://rest.api.transifex.com/resources'
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
        
        data = await web.post(url, json_data, self.headers)
        return data

    async def send_file(self, resource: str, content: str) -> Dict:
        resource_slug = f"o:{self.organization}:p:{self.project}:r:{resource}"
        json_data = {
            "data": {
                "attributes": {
                    "content": content,
                    "content_encoding": "text"
                },
                "relationships": {
                    "resource": {
                            "data": {
                                "id": resource_slug,
                                "type": "resources"
                            }
                    }
                },
                "type": "resource_strings_async_uploads"
            }
            }
        url = 'https://rest.api.transifex.com/resource_strings_async_uploads'
        data = await web.post(url, json_data, self.headers)
        return data

 
    async def send(self, resource: str, content: Dict) -> Dict:
        resources = await self.list_resources()
        if resource not in resources:
            await self.create_resource(resource)
        else:
            strings = await self.list_strings(resource)
            for key, value in strings.items():
                if key not in content.keys():
                    content[key] = value

        response = await self.send_file(resource, json.dumps(content))
            
        return response
    

class CreateUpdateStringsMixin:
    async def update_resource_strings(self, resource: str, content: List[tuple]):
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/vnd.api+json;profile="bulk"'
        url = 'https://rest.api.transifex.com/resource_strings'
        json_data = {
            "data": [
                {
                "attributes": {
                    "character_limit": 200,
                    "strings": {'other': value[0]},
                    "tags": []
                },
                "id": f"o:{self.organization}:p:{self.project}:r:{resource}:s:{value[1]}",
                "type": "resource_strings"
                }
            for value in content]
            }
        response = await web.patch(url, json_data, headers)
        return response

    async def create_resource_string(self, resource: str, content: List[tuple]):
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/vnd.api+json;profile="bulk"'
        url = 'https://rest.api.transifex.com/resource_strings'
        json_data = {
                "data": [
                    {
                    "attributes": {
                        "context": "frontpage,footer,verb",
                        "key": value[0],
                        "strings": {"other": value[1]},
                        "tags": []
                    },
                    "relationships": {
                        "resource": {
                        "data": {
                            "id": f"o:{self.organization}:p:{self.project}:r:{resource}",
                            "type": "resources"
                        }
                        }
                    },
                    "type": "resource_strings"
                    }
            for value in content]
            }
        response = await web.post(url, json_data, headers)
        return response
