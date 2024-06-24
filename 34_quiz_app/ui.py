from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)
        yes_image = PhotoImage(file="images/true.png")
        no_image = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_image, highlightthickness=0)
        self.no_button.grid(row=2, column=0)
        self.yes_button = Button(image=yes_image, highlightthickness=0)
        self.yes_button.grid(row=2, column=1)

        self.window.mainloop()
