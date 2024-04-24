from tkinter import *

def button_clicked():
    print ("I got clicked")
    my_label.config(text = input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font = ("Arial", 24, "bold"))
my_label.config(text = "New Text")
# my_label.pack(side = "left")
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)

#Button
button = Button(text = "Click me", command = button_clicked)
#button.pack(side = "left")
# if you create an object but forget to pack, place, or grid it, it won't show up
# button.place(x=0,y=100)
button.grid(column=0, row=2)
# note that you cannot grid and pack in the same window

#Entry
input = Entry(width=10)
print(input.get())
#input.pack(side = "left")
input.grid(column=0, row=1)










# This line is always at the end of the code
window.mainloop()