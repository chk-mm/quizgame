from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests

url = 'https://opentdb.com/api.php?amount=5'
response = requests.get(url)
datafromweb = response.json()

user_choice = input('Do you want to answer by ...\n1 - question from database\n2 - question from database api:')

if user_choice == '1':
    range_of_question = len(question_data)
    sources_of_data = question_data
    key = 'text'
    value = 'answer'
elif user_choice == '2':
    range_of_question = len(datafromweb['results'])
    sources_of_data = datafromweb['results']
    key = 'question'
    value = 'correct_answer'
else:
    print('Your input is incorrect, try again next time')



questionlist =[]

for i in range(range_of_question):
    question = Question(sources_of_data[i][key],sources_of_data[i][value])
    questionlist.append(question)

quizbrain = QuizBrain(questionlist)

while quizbrain.has_more_question():
    quizbrain.ask_question()
