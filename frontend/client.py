import requests
import os
from typing import Dict


def create_resource(categories):
    response = requests.post('http://127.0.0.1:8000/create_resource/', json={
        "items": [{'category': category} for category in categories]
    })
    return response


def get_categories() -> Dict:
    response = requests.get('http://127.0.0.1:8000/get_categories/')
    return response.json()


def main():
    os.system('clear')
    print('choose category to translate:')
    categories_map = get_categories()
    for key, value in categories_map.items():
        print(f'{key} : {value}')

    categories = []
    while True:
        category = input('category: ')
        categories.append(category)
        ex = input('Do you want to add another category [Y/n]')
        if ex != 'Y':
            break

    create_resource(categories)


if __name__ == '__main__':
    main()
