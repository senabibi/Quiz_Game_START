
class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list
       
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print(f"You got it!It is {user_answer.upper()}!!")
            
        else:
            print(f"No way!!The correct answer is {correct_answer.upper()}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n\n")
        
    def still_has_questions(self): 
        return (self.question_number)<len(self.question_list)
        
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        correct_answer=current_question.answer
        self.check_answer(user_answer,correct_answer)
    