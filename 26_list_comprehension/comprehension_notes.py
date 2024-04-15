
# # List Comprehension
# mylist = [1,2,3]
# # newlist = [new_item for item in original_list ]
# newlist = [item + 1 for item in mylist]
#
# print(mylist)
# print(newlist)


# name = 'Patrick'
# letters_list = [letter for letter in name]
# print(letters_list)
#
# # conditional list comprehension
# new_list = [new_item for item in list if test ]

# #Squared numbers:
# nums = range(1,10)
# squared_nums = [num**2 for num in nums]
# print (squared_nums)

# #filter even numbers
# nums = range(1,10)
# even_nums = [num for num in nums if num%2 == 0]
# print (even_nums)

# # data overlap
# num1s = range(1,10)
# num2s = range( 5,15)
# overlap = [num for num in num1s if num in num2s]
# print (overlap)

# Dictionary Comprehension Syntax
# new_dict = { new_key:new_value for item in list}

# names = ['Alex','Pat','Caroline','Dave','Angela']
# import random
# student_scores = {student:random.randint(1,100) for student in names}
#
# print (student_scores)
#
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60 }
#
# print (passed_students)
#
# sentence = 'How many letters are in each of these words?'
# result = {word:len(word) for word in sentence.split()}
# print(result)

# How to iterate over a Pandas DataFrame:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print (student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print (row.student)