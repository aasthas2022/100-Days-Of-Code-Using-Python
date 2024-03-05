## Day 17 - Section 17: Intermediate - The Quiz Project & the Benefits of OOP

# Class is simply a blueprint for creating an eventual object. Syntax: class <class_name>. Class names should be in pascal case. 
# Object intantiation: objname = classname()
# Adding attribute: objname.attributename = value (leveraged dot notation) , attribute is nothing but a variable that is associated with an obj.
# use pass keyword to have it as a placeholder for future code z
# Constructor is part of the blueprint that allows us to specify what should happen when our obj is contructed viz when an obj is initialized
# __init__(): used to initialize attributes, will be called everytime i create a new obj from the class 
# self binds attributes with the given argument. Can also initialize default value.
# A method (in a class), unlike a function must always have self as the first parameter

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        if current_question.check_answer(user_answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.questions)


from data import question_data

def main():
    questions = [Question(q["question"], q["correct_answer"]) for q in question_data]
    quiz = Quiz(questions)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    
main()
