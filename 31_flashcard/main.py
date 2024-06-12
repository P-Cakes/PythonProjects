from tkinter import *
from random import choice
import pandas

# import unittest
# class TestAssertions(unittest.TestCase):
#     def test_equals(self):
#         self.assertEqual(1, 1)
#         self.assertEqual("one string","one string")



# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

# Check if there is a file with words to learn
# If there is, load the words, which have potentially removed already learned words
# Else, load the original words and create a new file for next time

try :
    words = pandas.read_csv("data/words_to_learn.csv")
    to_learn = words.to_dict(orient="records")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
    to_learn = words.to_dict(orient="records")
    # create a new file for next
    new_word_file = pandas.DataFrame(to_learn)
    new_word_file.to_csv("data/words_to_learn.csv", index=False)

def is_known():
    to_learn.remove(current_card)
    new_word_file = pandas.DataFrame(to_learn)
    new_word_file.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer
    # In case of multiple clicks, cancel the previous timer
    window.after_cancel(flip_timer)
    current_card= choice(to_learn)
    canvas.itemconfig(card_img, image = card_front_img)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_text, text=current_card["French"])
    # Set a new timer for flipping the card
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_text, text=current_card["English"])
    canvas.itemconfig(card_img, image = card_back_img)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer  = window.after(3000, func = flip_card)

canvas = Canvas(height = 526, width = 800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image = card_front_img)
card_title = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text = "word", font = ("Ariel", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)

yes_image = PhotoImage(file="images/right.png")
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command = next_card )# ,command = lambda: next_card("no"))
no_button.grid(row = 1, column = 0)
yes_button = Button(image=yes_image, highlightthickness=0, command = is_known )# ,command = lambda: next_card("yes"))
yes_button.grid(row = 1, column = 1)

next_card()

# if __name__ == "__main__":
#     unittest.main()

window.mainloop()


