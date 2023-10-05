from typing import List
from question_model import Question

class QuizBrain:
    def __init__(self,questions: List[Question]):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def has_more_question(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False



    def ask_question(self):
        answer = input(f'{self.question_number+1}.{self.questions[self.question_number].text}Your answer?(True/False):')
        if answer.lower() == self.questions[self.question_number].answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print(f'The correct answer was {self.questions[self.question_number].answer}')
        self.question_number += 1
        print(f'Your current score is {self.score}/{self.question_number}')

    # question_bank = []

