import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
second_label = tkinter.Label(text="Second")
second_label.pack(side="left")


# Unlimited Arguments:
def add_unlimited_numbers(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add_unlimited_numbers(1, 2, 3, 4, 5)
add_unlimited_numbers(1, 2)

# **kwargs = many keyworded arguments
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print (n)

# This gives us a dictionary output
calculate(2, add=3, multiply = 5 )

class Car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.num_seats = kw.get('num_seats')



my_car = Car(make='Nissan',model='GTR')
print(my_car)
print(my_car.model)
print(my_car.num_seats)



def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x=10, y=64)

# Button

def button_clicked():
    print ("I got clicked")
    my_label.config(text = input.get())

button = tkinter.Button(text = "Click me", command = button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()
input.get()










# This line is always at the end of the code
window.mainloop()