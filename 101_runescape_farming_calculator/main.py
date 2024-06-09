from requests import get
from database import level_exp, trees, fruit_trees, tree_patches, fruit_tree_patches

def fetch_data():
    # ask the user to input a username
    username = 'PatttyCakes'  # input("Enter your username: ")
    api = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = get(api)
    # turn the response into a list by splitting on the newline character
    data = response.text.split("\n")
    # farming is the 20th skill so that is all the data we need
    farming_data = data[20].split(",")
    farming_level = farming_data[1]
    farming_exp = farming_data[2]
    return farming_level, farming_exp

farming_level = 99
farming_exp = 14693077

def set_goal():
    print ("Do you want to set a goal for 'level' or 'exp'?")
    goal = input("Enter 'level' or 'exp': ")
    while goal not in ['level', 'exp']:
        print ("Invalid input. Please enter 'level' or 'exp'")
        goal = input("Enter 'level' or 'exp': ")
    if goal == 'level':
        goal_level = input("Enter your goal level: ")
        goal_exp = level_exp[goal_level]
    elif goal == 'exp':
        goal_exp = input("Enter your goal exp: ")
        # Figure out what level this exp is

def highest_tree_run():
    high_tree = ''
    for tree in trees:
        if int(farming_level) >= trees[tree]['level']:
            high_tree = tree
    return high_tree

def highest_fruit_tree_run():
    high_fruit_tree = ''
    for fruit_tree in fruit_trees:
        if int(farming_level) >= fruit_trees[fruit_tree]['level']:
            high_fruit_tree = fruit_tree
    return high_fruit_tree


def tree_run():
    tree_to_run = highest_tree_run()
    print(f"Your highest tree run is {tree_to_run}")
    print(f"Your highest tree run is {trees[tree_to_run]['exp']} exp per check")
    count_tree_patches = 0
    # how do I get the number of true values in a dictionary?
    for patch in tree_patches:
        if tree_patches[patch]:
            count_tree_patches += 1
    print(f"You have {count_tree_patches} tree patches.")
    tree_run_exp = count_tree_patches * trees[tree_to_run]['exp']
    print(f"Your tree run exp is {tree_run_exp}")

def fruit_tree_run():
    fruit_tree_to_run = highest_fruit_tree_run()
    print(f"Your highest fruit tree run is {fruit_tree_to_run}")
    print(f"Your highest fruit tree run is {fruit_trees[fruit_tree_to_run]['exp']} exp per check")
    count_fruit_tree_patches = 0
    for patch in fruit_tree_patches:
        if fruit_tree_patches[patch]:
            count_fruit_tree_patches += 1
    print(f"You have {count_fruit_tree_patches} fruit tree patches.")
    fruit_tree_run_exp = count_fruit_tree_patches * fruit_trees[fruit_tree_to_run]['exp']
    print(f"Your fruit tree run exp is {fruit_tree_run_exp}")



tree_run()
fruit_tree_run()

# Goals 2:
# Add a GUI


# Goals 3:
# Add exp modifiers such as compost, magic secateurs, etc.
# Add additional exp from harvesting in addition to the checking exp
# store information in a database instead of simple structures


# Goals 4:
# Config the number of runs per day
# Add a time to 99 or time to exp calculator
# Add a profit and cost calculator
# Add modifier for protection payments
# also add chance of death
# balance this with the chance of death based on type of compost used

