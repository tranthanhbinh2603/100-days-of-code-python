from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

#Dùng OOP:
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Lấy câu đố
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quiz Brain')

        #Làm ui
        self.window.config(padx=20, pady=20)
        self.window.config(background=THEME_COLOR)

        self.label_score = Label(text='Score: 0', fg='white', font=('Arial', 10))
        self.label_score.config(background=THEME_COLOR)
        self.label_score.grid(column=1, row=0)

        self.questions = Canvas(height=250,width=300)
        self.questions_text = self.questions.create_text(145, 150,
             text='Test cho vui thôi',
             font=('Arial', 20, 'italic'),
             width=280)  # Căn giua bang 1 nua chieu rong canvas
        self.questions.grid(column=0, row=1, columnspan=2, pady=50)


        self.image_true = PhotoImage(file="images/true.png")
        self.true = Button(image=self.image_true, command=self.check_questions_button_true)
        self.true.grid(column=0, row=2)

        self.image_false = PhotoImage(file="images/false.png")
        self.false = Button(image=self.image_false, command=self.check_questions_button_false)
        self.false.grid(column=1, row=2)

        self.TheNextQuestion()

        self.window.mainloop()




    def TheNextQuestion(self):
        q_text = self.quiz.next_question()
        self.questions.itemconfig(self.questions_text, text=q_text)

    def check_questions_button_true(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer('True'):
                self.label_score.config(text=f'Score: {self.quiz.score}')
                self.questions.config(bg='green')
                self.window.after(1000, func=self.reset_layout)
            else:
                self.questions.config(bg='red')
                self.window.after(1000, func=self.reset_layout)

        else:
            self.questions.itemconfig(self.questions_text, text="Non question")

    def check_questions_button_false(self):
        if self.quiz.still_has_questions():
            if self.quiz.check_answer('False'):
                self.label_score.config(text=f'Score: {self.quiz.score}')
                self.questions.config(bg='green')
                self.window.after(1000, func=self.reset_layout)
            else:
                self.questions.config(bg='red')
                self.window.after(1000, func=self.reset_layout)
        else:
            self.questions.itemconfig(self.questions_text, text="Non question")
            #Câu lệnh mới
            self.false.config(state='disable')
            #self.questions.config(bg='green')

    def reset_layout(self):
        self.questions.config(bg='white')
        q_text = self.quiz.next_question()
        self.questions.itemconfig(self.questions_text, text=q_text)