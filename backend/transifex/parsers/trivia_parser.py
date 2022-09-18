from typing import Dict
from transifex.parsers import Parser
import json
import uuid


class TriviaParser(Parser):

    def parse(self, data: Dict) -> str:

        parsed = {}
        results = data['results']
        uuids = self.get_uuids(len(results))
        for j, result in enumerate(results):
            parsed[f'question:{uuids[j]}'] = result['question']
            parsed[f'correct_answer:{uuids[j]}'] = result['correct_answer']
            incorrect_answers = result['incorrect_answers']
            for i, answer in enumerate(incorrect_answers):
                parsed[f'incorrect_answers:{i}:{uuids[j]}'] = answer

        return json.dumps(parsed)

    def get_uuids(self, length) -> str:
        return [uuid.uuid4().hex for _ in range(length)]
    
    def reparse(self, output: str) -> Dict:
        pass
