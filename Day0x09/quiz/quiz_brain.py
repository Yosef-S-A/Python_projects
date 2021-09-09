class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.questions_list = q_list
		self.score = 0

	def next_question(self):
		current_question = self.questions_list[self.question_number]
		self.question_number += 1
		usr_answer = input("Q.{}: {} (True/False)?: ".format(self.question_number, current_question.text)).title()
		self.check_answer(usr_answer, current_question.answer)

	def still_has_question(self):
		return self.question_number < len(self.questions_list)

	def check_answer(self, response, correct_ans):
		if response == correct_ans:
			print("You got it right!")
			self.score += 1
		else:
			print("That's wrong.")

		print("The correct answer was: {}".format(correct_ans))
		print("Your current score is: {}/{}\n\n".format(self.score, self.question_number))
