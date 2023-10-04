from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



questionlist =[]

for i in range(len(question_data)):
    question = Question(question_data[i]['text'],question_data[i]['answer'])
    questionlist.append(question)

quizbrain = QuizBrain(questionlist)

while quizbrain.has_more_question():
    quizbrain.ask_question()

# print(questionlist)