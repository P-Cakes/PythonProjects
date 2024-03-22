


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

guesses = []
goal = input("What is the target word?")
goal_parts = list(goal)
lives = 6
output = []
for letter in goal_parts:
    output += ['_']
print (output)

while lives > 0:
    guess = input ("What do letter do you guess?")
    print (guess)
    print (goal_parts)
    if guess in goal_parts:
        guesses += guess 
        print("correct")
    if guess not in goal_parts: 
        lives -= 1
        print (f"incorrect, you have {lives} lives remaining.")
    for letter in range(len(goal_parts)):
        if guess == goal_parts[letter]:
            output[letter]=guess
    print(output)
    if output == goal_parts:
        print ("You win")
        break
    print(stages[lives])

if lives == 0:
    print ("You're dead")
    print (f"Goal was {goal}")