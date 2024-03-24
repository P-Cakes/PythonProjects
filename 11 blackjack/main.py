from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Return a random choice from cards list."""
    return random.choice(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def deal_cards():
    """Start with empty hands and use 
    deal_card() to give 2 random cards each"""
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    #hidden_card = deal_card()
    print (f"user has {user_cards} and computer has {computer_cards} and a hidden card")
    user_point = calculate_score(user_cards)
    computer_point = calculate_score(computer_cards)
    print (f"user has {user_point} points vs computer's {computer_point} ")
    return user_cards, computer_cards


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(hand):
    """Return score of inputted hand(list) of cards"""
    hand_score = 0
    #check for blackjack at start
    if hand == [10,11] or hand == [11,10]:
        return 0
    
    for card in hand:
        hand_score += card
        if hand_score > 21:
            if 11 in hand:
                print ("ace")
            print ("Bust")
    return hand_score 



def play_blackjack():
    print(logo)
    user_cards , computer_cards = deal_cards()
    user_playing = True
    user_score = calculate_score(user_cards)
    while user_playing is True and user_score < 22:
        if user_score == 21:
            print ("Blackjack!")
        elif input(f"You have {user_cards}. Your score is {user_score}. Do you want to hit?\n") == 'n':
            user_playing = False
        else:
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

    computer_score = calculate_score(computer_cards)
    if computer_score == 0:
        print ("Dealer has blackjack!")
        if input("Keep playing? 'y' or 'n' \n") == 'y':
                play_blackjack()
    if computer_score > user_score and computer_score < 22:
        print ('computer wins')
    while computer_score < 16:
        print(f"Computer has {computer_score} points and must draw.")
        computer_cards.append(deal_card())
        print (f"computer has {computer_cards}")
        computer_score = calculate_score(computer_cards)
    if computer_score > user_score and computer_score < 22:
        print ('computer wins appending')
    elif computer_score > 21:
        print ('computer busts')
    elif computer_score == user_score:
        print ('Draw')
    else: 
        print (f"computer score is {computer_score}")
        if computer_score > user_score:
            print ("Computer wins!")
        else:
            print ("You win!")
    if input("Keep playing? 'y' or 'n' \n") == 'y':
        play_blackjack()

           


    
    

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

play_blackjack()

