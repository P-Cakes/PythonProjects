
import random
from art import logo as logo
from art import vs as vs
import gamedata
from replit import clear

#Dictionary of values

#Randint to generate random integer

#set score to 0

# compare random value to the next random value
#ask user which is higher
# if correct, score += 1
#   new randint
#   new compare
# else
# restart, score back to 0

def play_game():
    clear()
    print (logo)
    score = 0
    continue_game = False
    if input("Do you want to play? 'y' or 'n'") == 'y':
        continue_game = True
        compare= (random.randint(0,len(gamedata.data)))
        compare2=(random.randint(0,len(gamedata.data)))
    while continue_game is True:
        compare= compare2
        compare2=(random.randint(0,len(gamedata.data)))
        print (f"Option A: {gamedata.data[compare]['name']} is a {gamedata.data[compare]['description']} from {gamedata.data[compare]['country']}")
        print (vs)
        print (f"Option B: {gamedata.data[compare2]['name']} is a {gamedata.data[compare2]['description']} from {gamedata.data[compare2]['country']}")
        choice = input(f"{gamedata.data[compare]['name']} has {gamedata.data[compare]['follower_count']} followers. Does {gamedata.data[compare2]['name']} have more?\nWho has more followers? 'a' or 'b'?")
        if choice == 'a' and gamedata.data[compare]['follower_count'] > gamedata.data[compare2]['follower_count']:
            score += 1
            clear()
            print(f"Correct.  You now have {score} points.")
        elif choice == 'b' and gamedata.data[compare]['follower_count'] < gamedata.data[compare2]['follower_count']:
            score += 1
            clear()
            print(f"Correct.  You now have {score} points.")
        else:
            continue_game = False
            print(f"Incorrect.  You end the game with {score} points.")



play_game()