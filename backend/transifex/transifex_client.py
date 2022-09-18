from typing import List, Dict
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

    async def list_resourcers(self) -> List[str]:
        url = 'https://rest.api.transifex.com/resources'
        params = {'filter[project]': f'o:{self.organization}:p:{self.project}'}
        data = await web.get(url, params, self.headers)
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

    async def send(self, resource: str, content: str):
        resources = await self.list_resourcers()
        if resource not in resources:
            await self.create_resource(resource)
        response = await self.send_file(resource, content)
        return response
