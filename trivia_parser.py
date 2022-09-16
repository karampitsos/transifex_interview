from typing import Dict

class TriviaParser:
    
    def parse(self, data: Dict):
        results = data['results']
        for result in results:
            incorrect_answers = result['incorrect_answers']
            question = result['question']
            correct_answer = result['correct_answer']
        
        return data




{'response_code': 0,
 'results': [{'category': 'Entertainment: Books',
              'correct_answer': 'Charlotte Bront&euml;',
              'difficulty': 'hard',
              'incorrect_answers': ['Emily Bront&euml;',
                                    'Jane Austen',
                                    'Louisa May Alcott'],
              'question': 'The novel &quot;Jane Eyre&quot; was written by what '
                          'author? ',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'John Steinbeck ',
              'difficulty': 'medium',
              'incorrect_answers': ['George Orwell',
                                    'Mark Twain ',
                                    'Harper Lee'],
              'question': 'The novel &quot;Of Mice And Men&quot; was written '
                          'by what author? ',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'John Green',
              'difficulty': 'easy',
              'incorrect_answers': ['Stephenie Meyer',
                                    'Suzanne Collins',
                                    'Stephen Chbosky'],
              'question': 'Who wrote the young adult novel &quot;The Fault in '
                          'Our Stars&quot;?',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': '42',
              'difficulty': 'medium',
              'incorrect_answers': ['Loving everyone around you',
                                    'Chocolate',
                                    'Death'],
              'question': 'According to The Hitchhiker&#039;s Guide to the '
                          'Galaxy book, the answer to life, the universe and '
                          'everything else is...',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'Maximum Ride',
              'difficulty': 'medium',
              'incorrect_answers': ['Harry Potter',
                                    'The Legend of Xanth',
                                    'The Bartemaeus Trilogy'],
              'question': 'Which of these book series is by James Patterson?',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'Answer a riddle',
              'difficulty': 'medium',
              'incorrect_answers': ['Rhythmically tap barrels with a wand',
                                    'Speak a password',
                                    'Knock in sequence'],
              'question': 'In the &quot;Harry Potter&quot; novels, what must a '
                          'Hogwarts student do to enter the Ravenclaw Common '
                          'Room?',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'A Clash of Kings',
              'difficulty': 'easy',
              'incorrect_answers': ['A Dance with Dragons',
                                    'A Storm of Swords',
                                    'A Feast for Crows'],
              'question': 'What&#039;s the second book in George R. R. '
                          'Martin&#039;s &#039;A Song of Ice and Fire&#039; '
                          'series?',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'True',
              'difficulty': 'easy',
              'incorrect_answers': ['False'],
              'question': '&quot;Green Eggs and Ham&quot; consists of only 50 '
                          'different words.',
              'type': 'boolean'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'Steven Erikson',
              'difficulty': 'medium',
              'incorrect_answers': ['Ian Cameron Esslemont',
                                    'George R. R. Martin',
                                    'J. R. R. Tolkien'],
              'question': 'Who is the author of the series &quot;Malazan Book '
                          'of the Fallen&quot;?',
              'type': 'multiple'},
             {'category': 'Entertainment: Books',
              'correct_answer': 'Leo Tolstoy',
              'difficulty': 'medium',
              'incorrect_answers': ['Fyodor Dostoyevsky',
                                    'Alexander Pushkin',
                                    'Vladimir Nabokov'],
              'question': 'Which Russian author wrote the epic novel War and '
                          'Peace?',
              'type': 'multiple'}]}