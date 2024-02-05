from question_model import Qustion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Qustion(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if quiz.still_has_questions() is False:
    print(f"You've completed the quiz\nYour final score is {quiz.score}")

# quiz.next_question()