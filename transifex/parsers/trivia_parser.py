from typing import Dict
from transifex.parsers import Parser
import hashlib


class TriviaParser(Parser):

    def parse(self, input: Dict) -> Dict[str, str]:

        output = {}
        trivias = input['results']
        for trivia in trivias:
            question: str = trivia['question']
            correct_answer = trivia['correct_answer']
            incorrect_answers = trivia['incorrect_answers']

            hash = hashlib.md5(question.encode()).hexdigest()

            output[f'question:{hash}'] = question
            output[f'correct_answer:{hash}'] = correct_answer
            for i, answer in enumerate(incorrect_answers):
                output[f'incorrect_answers:{i}:{hash}'] = answer

        return output

    def reparse(self, input: Dict[str, str]) -> Dict:
        output = {}
        hashes = []
        for key, body in input.items():
            keys = key.split(":")
            hash = keys[-1]
            if hash not in hashes:
                hashes.append(hash)
                output[hash] = {}

            type = keys[0]
            if type == 'incorrect_answers':
                if type not in output[hash]:
                    output[hash][type] = []
                    
                output[hash][type].append(body)
            else:
                output[hash][type] = body
        return output
