#B1: Get lại tuu vien get dũ liẹu
#B2: Viết UI theo kiểu OOP
#B3: Thực hiện lấy lại code ở QuizBrain rồi code thêm phần đổi câu hỏi
#B4: Hiển thị điểm (Sử dụng hàm bên trong quiz_brain)
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import *

#Thực hiện get:
question_data = question_data


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_in = QuizInterface(quiz)


#quiz_in.TheNextQuestion()

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
