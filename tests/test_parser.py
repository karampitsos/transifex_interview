import pytest
from typing import Dict
import json
from transifex.parsers import TriviaParser


@pytest.fixture
def input() -> Dict:
    with open('tests/data/trivia_input.json', 'r') as file:
        _input = json.load(file)
    return _input

@pytest.fixture
def output() -> str:
    with open('tests/data/trivia_output.json', 'r') as file:
        _output = file.read()
    return _output


def test_trivia_parser(input, output):

    assert TriviaParser().parse(input) == output


def test_trivia_reparse(data, output):
    assert True
