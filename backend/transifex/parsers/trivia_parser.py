from typing import Dict
from transifex.parsers import Parser
import hashlib


class TriviaParser(Parser):

    def parse(self, data: Dict) -> Dict:

        parsed = {}
        results = data['results']
        for result in results:
            question: str = result['question']
            hash = hashlib.md5(question.encode()).hexdigest()
            parsed[f'question:{hash}'] = question
            parsed[f'correct_answer:{hash}'] = result['correct_answer']
            incorrect_answers = result['incorrect_answers']
            for i, answer in enumerate(incorrect_answers):
                parsed[f'incorrect_answers:{i}:{hash}'] = answer

        return parsed

    
    def reparse(self, output: str) -> Dict:
        pass
