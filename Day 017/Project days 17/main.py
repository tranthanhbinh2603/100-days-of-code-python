from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data = []
for question in question_data:
    text = question["text"] #Đổi chìa khoá là được
    answer = question["answer"]
    ques = Question(text, answer)
    data.append(ques)

quizBrain = QuizBrain(data)
while quizBrain.still_has_question():
    quizBrain.next_question()

print(f'You complete this Quiz.')
print(f'The final score is {quizBrain.score}/{len(question_data)}')