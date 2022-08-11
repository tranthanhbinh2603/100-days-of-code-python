import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current.text} (True/False): ")
        self.check_answer(user_answer, current.answer)


    def still_has_question(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user, correct):
        if (user.lower() == correct.lower()):
            print('You got it right')
            self.score += 1
        else:
            print('That''s wrong')
        print(f'Te correct answer was: {correct}')
        print(f'Your current score is:  {self.score}/{self.question_number}\n')


