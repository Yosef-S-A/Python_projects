#!/usr/bin/python3

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
	question = data["question"]
	answer = data["correct_answer"]
	new_question = Question(question, answer)
	question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
	quiz.next_question()

print("You've completed the quiz")
print("Your final score was: {}/{}".format(quiz.score, quiz.question_number))
