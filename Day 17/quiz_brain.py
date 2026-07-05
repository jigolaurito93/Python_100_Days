from tabnanny import check


class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list # List of Objects
        self.user_score = 0
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print(f"You got it right!")
            self.user_score += 1
        else:
            print(f"You got it wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
    
    def announce_result(self):
        print(f"You've completed the quiz.")
        print(f"Your final score is: {self.user_score}/{self.question_number}")


