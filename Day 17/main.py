from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    print("\n" * 2)
quiz_brain.announce_result()
