import math

from requests import get
from database import level_exp, trees, fruit_trees, tree_patches, fruit_tree_patches
from math import ceil


def fetch_data():
    """ Fetch the farming level and exp from the OSRS hiscores API for the inputted username. """
    # ask the user to input a username
    username = 'PatttyCakes'  # input("Enter your username: ")
    api = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = get(api)
    # turn the response into a list by splitting on the newline character
    data = response.text.split("\n")
    # farming is the 20th skill so that is all the data we need
    farming_data = data[20].split(",")
    current_farming_exp = int (farming_data[2])
    return current_farming_exp


# hard coding so that I don't constantly ping the api while testing
farming_level = 99
current_farming_exp = 14693077


def set_goal():
    """ Set the goal for the farming calculator. """
    print("Do you want to set a goal for 'level' or 'exp'?")
    goal = input("Enter 'level' or 'exp': ")
    while goal not in ['level', 'exp']:
        print("Invalid input. Please enter 'level' or 'exp'")
        goal = input("Enter 'level' or 'exp': ")
    if goal == 'level':
        goal_level = input("Enter your goal level: ")
        goal_exp = int(level_exp[goal_level])
        while int(goal_exp) <= current_farming_exp:
            print("Invalid input. Your goal level must be greater than your current level.")
            goal_level = input("Enter your goal level: ")
            goal_exp = int(level_exp[goal_level])
        return goal_exp
    elif goal == 'exp':
        goal_exp = int(input("Enter your goal exp: "))
        while int(goal_exp) <= current_farming_exp:
            print("Invalid input. Your goal exp must be greater than your current exp.")
            goal_exp = int(input("Enter your goal exp: "))
        return goal_exp


def highest_tree_run():
    """ Determine the highest tree that can be planted based on the farming level."""
    high_tree = ''
    for tree in trees:
        if int(farming_level) >= trees[tree]['level']:
            high_tree = tree
    return high_tree


def highest_fruit_tree_run():
    """ Determine the highest fruit tree that can be planted based on the farming level. """
    high_fruit_tree = ''
    for fruit_tree in fruit_trees:
        if int(farming_level) >= fruit_trees[fruit_tree]['level']:
            high_fruit_tree = fruit_tree
    return high_fruit_tree


def tree_patches_available():
    """ Determine the number of tree patches available. """
    count_tree_patches = 0
    for patch in tree_patches:
        if tree_patches[patch]:
            count_tree_patches += 1
    return count_tree_patches


def fruit_tree_patches_available():
    """ Determine the number of fruit tree patches available. """
    count_fruit_tree_patches = 0
    for patch in fruit_tree_patches:
        if fruit_tree_patches[patch]:
            count_fruit_tree_patches += 1
    return count_fruit_tree_patches


def runs_to_goal():
    """ Calculate the number of runs needed to reach the goal. """
    goal_exp = set_goal()
    tree_run_exp = trees[highest_tree_run()]['exp']
    fruit_tree_run_exp = fruit_trees[highest_fruit_tree_run()]['exp']
    tree_patches = tree_patches_available()
    fruit_tree_patches = fruit_tree_patches_available()
    total_exp_from_tree_and_fruit_run = (tree_run_exp * tree_patches) + (fruit_tree_run_exp * fruit_tree_patches)
    exp_to_goal = goal_exp - current_farming_exp
    runs = math.ceil( exp_to_goal / total_exp_from_tree_and_fruit_run)
    print(f"You can plant {tree_patches} {highest_tree_run()} trees and {fruit_tree_patches} {highest_fruit_tree_run()} trees per run.")
    print(f"This will give you {total_exp_from_tree_and_fruit_run} exp per run.")
    print(f"Your current exp is {current_farming_exp} so you have {exp_to_goal} exp remaining until your goal of {goal_exp}.")
    print(f"You need to do {runs} runs to reach your goal.")

runs_to_goal()
# Goals 2:
# Add a GUI


# Goals 3:
# Add exp modifiers such as compost, magic secateurs, etc.
# Add additional exp from harvesting in addition to the checking exp
# store information in a database instead of simple structures


# Goals 4:
# Consider the logic that will be needed for virtual levels
# Config the number of runs per day
# Add a time to 99 or time to exp calculator
# Add a profit and cost calculator
# Add modifier for protection payments
# also add chance of death
# balance this with the chance of death based on type of compost used
