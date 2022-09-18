import pytest
from typing import Dict
import json
from transifex.parsers import TriviaParser


@pytest.fixture
def data() -> Dict:
    with open('tests/inputs/trivia_input.json', 'r') as file:
        _data = json.load(file)
    return _data

@pytest.fixture
def output() -> str:
    _output = json.dumps({
        'question:1': 'What was the title of ABBA`s first UK hit single?',
        'correct_answer:1': 'Waterloo',
        'incorrect_answers:0:1': 'Mamma Mia',
        'incorrect_answers:1:1': 'Fernando',
        'incorrect_answers:2:1': 'Dancing Queen',

        'question:2': 'Who was not in the band &quot;The Smiths&quot;?',
        'correct_answer:2': 'Martin Chambers',
        'incorrect_answers:0:2': 'Morrissey',
        'incorrect_answers:1:2': 'Andy Rourke',
        'incorrect_answers:2:2': 'Mike Joyce',
        
        'question:3': 'In Mean Girls, who has breasts that tell when its raining?',
        'correct_answer:3': 'Karen Smith',
        'incorrect_answers:0:3': 'Gretchen Weiners',
        'incorrect_answers:1:3': 'Janice Ian',
        'incorrect_answers:2:3': 'Cady Heron',
        
        'question:4': 'Make You Feel My Love was originally written and performed by which singer-songwriter?',
        'correct_answer:4': 'Bob Dylan',
        'incorrect_answers:0:4': 'Elvis',
        'incorrect_answers:1:4': 'Adele',
        'incorrect_answers:2:4': 'Billy Joel',

        'question:5': 'Panic! At the Disco&#039;s sixth album &quot;Pray For The Wicked&quot; was released on which date?',
        'correct_answer:5': 'June 22, 2018',
        'incorrect_answers:0:5': 'May 9, 2018',
        'incorrect_answers:1:5': 'March 13, 2018',
        'incorrect_answers:2:5': 'February 21, 2018',
        })
    return _output


def test_trivia_parser(data, output, mocker):
    mocker.patch(
        'transifex.parsers.trivia_parser.TriviaParser.get_uuids',
        return_value= ['1','2','3','4','5']
        )
    
    assert TriviaParser().parse(data) == output

def test_trivia_reparse(data, output):
    assert True