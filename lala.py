from transifex.parsers import TriviaParser
import json
from pprint import pprint


with open('tests/data/trivia_input.json', 'r') as file:
    input = json.load(file)

print(TriviaParser().parse(input))