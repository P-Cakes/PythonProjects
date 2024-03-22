



guesses = []
goal = input("What is the target word?")
goal_parts = list(goal)
lives = 6

while lives >= 0:
    guess = input ("What do letter do you guess?")
    print (guess)
    print (goal_parts)
    if guess in goal_parts:
        guesses += guess 
        print("correct")
    else: 
        lives -= 1
        print (f"incorrect, you have {lives} lives remaining.")

