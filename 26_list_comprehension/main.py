student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

# nato_dict = {}
# bad_nato_dict = {}
nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_file.iterrows()}
bad_nato = {row.letter:row.bad for (index,row) in nato_file.iterrows()}
print (nato_dict)
print (bad_nato)
# for (index, row) in nato_file.iterrows():
#     nato_dict.append(yo)
#     print (row.letter)
#     print (row.code)
#     print (row.bad)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def get_nato():
    word = input('Input word you want phonetic letters for: ').upper()
    style = input(f"Word is {word}, do you want 'nato' or 'bad' letters?")
    while style not in ['nato','bad','exit']:
        style = input (f"Word is {word}, do you want 'nato' or 'bad' letters? Or 'exit'.")
    if style == 'exit':
        print ("Exiting")
        return 'exit'
    try:
        if style == 'nato':
            output = [nato_dict[letter] for letter in word]
        else:
            output = [bad_nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the input word please.")
        get_nato()
    else:
        print (output)
    go_again = input("Go again? 'yes', 'no': ")
    if go_again == 'yes':
        get_nato()

get_nato()