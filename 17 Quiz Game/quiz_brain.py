

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        #q_list expected to be question_bank from main
        self.question_list = q_list 
        self.score = 0

    def still_has_questions(self):
        """Return True if we still have questions left.
        Else return False"""
        return len(self.question_list) > self.question_number


    def next_question(self):
        current_question = self.question_list[self.question_number]
        #We have to iterate up anyway, so may as well do it early so that the print
        #question number starts at 1, instead of 0, for Q1
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)")
        if user_answer == current_question.answer:
            self.score += 1
            print ("Correct")
        else:
            print ("Incorrect")



