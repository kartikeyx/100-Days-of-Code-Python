class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.questions_list = q_list
    self.score = 0

  def still_has_questions(self):
    return self.question_number < len(self.questions_list)
     
  def check_answer(self, c_answer, u_answer):
    if c_answer == u_answer:
      self.score+=1
      print("You got it right.")
      print(f"The correct answer is{c_answer}.")
      print(f"Your current score is {self.score}/{self.question_number}")
    else:
      print("You got it wrong.")
      print(f"The correct answer is{c_answer}.")
      print(f"Your current score is {self.score}/{self.question_number}")


  def next_question(self):
    current_question = self.questions_list[self.question_number]
    self.question_number+=1
    u_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
    check_answer(current_question.answer, u_answer)

  