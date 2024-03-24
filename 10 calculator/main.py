
def add(n1,n2):
    """Add two numbers together"""
    return n1 + n2 

def subtract(n1,n2):
    """Subtract n2 from n1"""
    return n1 - n2

def multiply(n1,n2):
    """Multiply two numbers by one another"""
    return n1 * n2 

def divide(n1,n2):
    "Divide n1 by n2"
    return n1 / n2

#Dictionary of our math operations
operations = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}

num1 = float(input("What is the first number?: "))
num2 = float(input("What is the second number?: "))


operation_symbol = input ("Pick an operation: ")
#Use our dictionary to define the operation function
operation = operations[operation_symbol]
answer = operation(num1,num2)

print (f"{num1} {operation_symbol} {num2} = {answer}")

continue_loop = True
while continue_loop is True:
    continue_question = input ("Would you like to continue? 'y' or 'n'?")
    if continue_question == 'n':
        continue_loop = False
    else:
        operation_symbol = input ("Pick another operation: ")
        num3 = float(input("Pick another number: "))
        operation = operations[operation_symbol]
        new_answer = operation(answer,num3)
        print (f"{answer} {operation_symbol} {num3} = {new_answer}")
        answer = new_answer 


