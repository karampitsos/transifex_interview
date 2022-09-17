from typing import Dict
import json
import uuid


class TriviaParser:
    
    def parse(self, data: Dict) -> str:

        parsed = {}
        results = data['results']
        for result in results:
            id = self.get_uuid()
            incorrect_answers = result['incorrect_answers']
            question = result['question']
            correct_answer = result['correct_answer']
            parsed[f'question:{id}'] = question
            parsed[f'correct_answer:{id}'] = correct_answer
            for i, answer in enumerate(incorrect_answers):
                parsed[f'incorrect_answers:{i}:{id}'] = answer
        
        return json.dumps(parsed)
    
    def get_uuid(self) -> str:
        return uuid.uuid4().hex
