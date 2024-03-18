rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

user_choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n") )
print (f"You chose {user_choice}")
print (game_images[user_choice])

computer_choice = random.randint(0,2)
print (f"Computer chose {computer_choice}")
print (game_images[computer_choice])

if user_choice == computer_choice:
    print ("Tied!")
elif user_choice == 0:
    if computer_choice == 1:
        print ("Computer wins!")
    elif computer_choice == 2:
        print ("You win!")
elif user_choice == 1:
    if computer_choice == 2:
        print ("Computer wins!")
    elif computer_choice == 0:
        print ("You win!")
elif user_choice == 2: 
    if computer_choice == 0:
        print ("Computer Wins!")
    elif computer_choice == 1:
        print ("You win!")
else:
    print ("You typed an invalid number. You lose!")



