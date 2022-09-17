from typing import Dict
from transifex.parsers import Parser
import json
import uuid


class TriviaParser(Parser):

    def parse(self, data: Dict) -> str:

        parsed = {}
        results = data['results']
        for result in results:
            id = self.get_uuid()
            parsed[f'question:{id}'] = result['question']
            parsed[f'correct_answer:{id}'] = result['correct_answer']
            incorrect_answers = result['incorrect_answers']
            for i, answer in enumerate(incorrect_answers):
                parsed[f'incorrect_answers:{i}:{id}'] = answer

        return json.dumps(parsed)

    def get_uuid(self) -> str:
        return uuid.uuid4().hex
