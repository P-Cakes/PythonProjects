from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    new_question = Question(questions['text'],questions['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print(F"You answered {quiz.score} questions correctly.")
