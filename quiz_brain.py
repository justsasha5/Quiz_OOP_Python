class QuizChecker:
    def run_check(self, ques_answ):
        score = 0
        count = 1
        for question in ques_answ:
            user_answer = input(question.text)
            user_answer = user_answer.lower()
            if user_answer.isalpha() != True:
                print("Please input a,b or c")
                return
            if user_answer == question.answer:
                score += 1
            print(f"You got: {score} / {count}")
            print(f"Correct Answer is {question.answer}")
            count += 1
