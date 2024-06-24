from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # As we init, we can define that the quiz_brain must be a QuizBrain object
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)

        yes_image = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=yes_image, highlightthickness=0, command= self.answer_yes)
        self.yes_button.grid(row=2, column=1)

        no_image = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_image, highlightthickness=0, command= self.answer_no)
        self.no_button.grid(row=2, column=0)

        # Populate the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            new_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_question_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
    def answer_yes(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def answer_no(self):
        self.quiz.check_answer("False")
        self.get_next_question()
