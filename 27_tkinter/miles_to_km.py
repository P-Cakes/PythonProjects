from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles = Label(text = "Miles")
kilometers = Label(text = "Kilometers")
equal = Label(text = "is equal to")

miles_input = Entry()

def button_clicked():
    miles_val = int(miles_input.get())
    kilo_val = round(miles_val * 1.60934,2)
    kilometer_result.config(text = kilo_val)

kilometer_result = Label(text = "0")

calculate_button = Button(text="Calculate", command=button_clicked)

miles.grid(column= 2, row = 1)
kilometers.grid(column=2,row =2 )
equal.grid(column= 0, row= 2)
miles_input.grid(column= 1, row = 1)
kilometer_result.grid(column=1,row=2)
calculate_button.grid(column=1,row=3)





# This line is always at the end of the code
window.mainloop()