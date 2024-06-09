from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_clicked():
    pass
#     global reps
#     global timer
#     reps = 0
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text = "00:00")
#     title_label.config(text = "Timer")
#     check_marks.config(text = "")




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text= "Work")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text= "Long Break")
    else:
        count_down(short_break_sec)
        timer_label.config(text= "Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    global timer
    if len(str(seconds)) == 1:
        seconds = '0' + str(seconds)
    timer = canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
#window.minsize(width=200, height=224)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


timer_label = Label(text = "Timer", fg= GREEN, bg=YELLOW, font = (FONT_NAME, 35, "bold"))
timer_label.grid(column= 1, row = 0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_button_clicked, highlightthickness=0)
reset_button.grid(column=2,row=2)

num_checks = (reps // 2 ) * "✔"
check_marks = Label(text= num_checks, fg= GREEN, bg= YELLOW)
check_marks.grid(column=1,row=3)

# This line is always at the end of the code
window.mainloop()