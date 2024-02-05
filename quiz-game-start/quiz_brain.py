class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


# or it can be return self.question_number < len(self.question_list)
#cuz f.e. a =3 b = 5 -> return b > a -> True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}:{current_question.text}:(True/False)\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer was right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}!")
        print(f"Your curent score is {self.question_number}/{self.score}.")
        print("\n")