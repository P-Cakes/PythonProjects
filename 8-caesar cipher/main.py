alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
direction = ''
while direction not in ('encode','decode'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
'''

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode": 
        shift_amount *= -1 
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position >= 26:
                new_position -=25
            if new_position < 0:
                new_position +=25
            end_text += alphabet[new_position]
        else: end_text += letter  
    print (f"The {cipher_direction}d text is {end_text}")



'''
def encrypt(text,shift):
    new_text =''
    for letter in text:
        position = alphabet.index(letter)
        position += shift
        if position >= 26: 
            position -= 25
        new_text += alphabet[position]
    print (f"The encoded text is {new_text}")

def decrypt(text,shift):
    new_text = ''
    for letter in text: 
        position = alphabet.index(letter)
        position -= shift
        if position < 0: 
            position += 25
        new_text += alphabet[position]
    print (f"The decoded text is {new_text}")

if direction == 'encode':
    encrypt(text,shift)
if direction == 'decode':
    decrypt(text,shift)

'''



#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue = True
while should_continue:
  direction = ''
  while direction not in ('encode','decode'):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  go_again = ''
  while go_again not in ('yes','no'):
      go_again = input("Would you like to go again? 'yes' or 'no' ")
  if go_again == 'no':
      should_continue = False
      print("Goodbye")





