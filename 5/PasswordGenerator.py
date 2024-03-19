#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


print ('Welcome to the PyPassword Generator!')
letters_count = int(input ('How many letters would you like in your password?\n') )
numbers_count = int(input ('How many numbers would you like in your password?\n') )
symbols_count = int(input ('How many symbols would you like in your password?\n') )

password = ''
for item in range(letters_count):
    password += letters[random.randint(0,(len(letters))-1)]
for item in range(numbers_count):
    password += numbers[random.randint(0,(len(numbers))-1)]
for item in range(symbols_count):
    password += symbols[random.randint(0,(len(symbols))-1)]


print (f"Your simple password is {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = []
for item in range(letters_count):
    password_list += [letters[random.randint(0,(len(letters))-1)]]
for item in range(numbers_count):
    password_list += [numbers[random.randint(0,(len(numbers))-1)]]
for item in range(symbols_count):
    password_list += [symbols[random.randint(0,(len(symbols))-1)]]

random.shuffle(password_list)

password = ''
for item in range(len(password_list)):
    password += password_list[item]

print (f"Your hard password is {password}")