import random

def play_game():
    target = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5

    while attempts > 0:
        print (f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        if guess == target:
            print(f"You got it! The answer was {target}.")
            return
        elif guess < target:
            print ("Too Low")
            attempts -= 1
        elif guess > target:
            print("Too high")
            attempts -= 1


continue_game = True

while continue_game is True:
    play_game()
    if input('Play again?\n')== 'n' :
        continue_game = False
