import math

from requests import get
from database import level_exp, trees, fruit_trees, tree_patches, fruit_tree_patches
from math import ceil
import tkinter as tk

# hard coding so that I don't constantly ping the api while testing
username = "PatttyCakes"
farming_level = 99
current_farming_exp = 14000000
goal_exp = 20000000
def set_username():
    global username
    username = username_entry.get()
    print(f"Username set to {username}")
    current_username.config(text=f"Current Username: {username}")
    current_farming_exp = fetch_data()
    current_farming_exp_label.config(text=f"Current Farming Exp: {current_farming_exp}")

def fetch_data():
    """ Fetch the farming level and exp from the OSRS hiscores API for the inputted username. """
    api = f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}"
    response = get(api)
    global current_farming_exp
    # turn the response into a list by splitting on the newline character
    data = response.text.split("\n")
    # farming is the 20th skill so that is all the data we need
    farming_data = data[20].split(",")
    current_farming_exp = int (farming_data[2])
    return current_farming_exp


def set_goal():
    """ Set the goal for the farming calculator. """
    print("Do you want to set a goal for 'level' or 'exp'?")
    goal = input("Enter 'level' or 'exp': ")
    if goal == "cancel":
        return
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

def quick_update_goal():
    """ Simple helper function to quickly update the goal exp in tkinter"""
    global goal_exp
    goal_exp = int(goal_exp_entry.get())
    print (f"goal exp is {goal_exp}")
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
    # update the tkinter labels
    tree_label.config(text=f"Trees: {highest_tree_run()}")
    fruit_tree_label.config(text=f"Fruit Trees: {highest_fruit_tree_run()}")
    exp_per_run_label.config(text=f"Exp per run: {total_exp_from_tree_and_fruit_run}")
    runs_to_goal_label.config(text=f"Runs to goal: {runs}")

# Goals 2:
# Add a GUI


root = tk.Tk()
root.title("Farming Calculator")
root.geometry("800x600")
# create a grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# create a frame
frame = tk.Frame(root, bg='#32a852')
frame.grid(row=0, column=0, sticky="nsew")
# create a label
label = tk.Label(frame, text="Farming Calculator", font=("Arial", 24))
label.pack(pady=10)
# add a textbox to input username
username_label = tk.Label(frame, text="Enter your username:", font=("Arial", 12))
username_label.pack(pady=10)
# create an Entry widget for username input
username_entry = tk.Entry(frame, font=("Arial", 12))
username_entry.pack(pady=0)
# create a button to fetch data
username_button = tk.Button(frame, text="Set Username", font=("Arial", 12), command=set_username)
username_button.pack(pady=10)
current_username = tk.Label(frame, text=f"Current Username: {username}", font=("Arial", 12))
current_username.pack(pady=10)
# Display the current farming level and exp
current_farming_exp_label = tk.Label(frame, text=f"Current Farming Exp: {current_farming_exp}", font=("Arial", 12))
current_farming_exp_label.pack(pady=10)
# What is the goal exp
goal_exp_entry = tk.Entry(frame, font=("Arial", 12))
goal_exp_entry.pack(pady=10)
# Fill the goal_exp_entry with goal_exp
goal_exp_entry.insert(0, str(goal_exp))
# create a button to set the goal
goal_button = tk.Button(frame, text="Set Goal", font=("Arial", 12), command=quick_update_goal)
goal_button.pack(pady=10)
# create a button to calculate the runs to goal
calculate_button = tk.Button(frame, text="Calculate Runs to Goal", font=("Arial", 12), command=runs_to_goal)
calculate_button.pack(pady=10)
# display trees and fruit trees in tkinter
# create a label
tree_label = tk.Label(frame, text="Trees", font=("Arial", 12))
tree_label.pack(pady=10)
# create a label
fruit_tree_label = tk.Label(frame, text="Fruit Trees", font=("Arial", 12))
fruit_tree_label.pack(pady=10)
# create a label for exp gained per run
exp_per_run_label = tk.Label(frame, text="Exp per run", font=("Arial", 12))
exp_per_run_label.pack(pady=10)
# create a label for runs to goal
runs_to_goal_label = tk.Label(frame, text="Runs to goal", font=("Arial", 12))
runs_to_goal_label.pack(pady=10)
# run the main loop

root.mainloop()

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
