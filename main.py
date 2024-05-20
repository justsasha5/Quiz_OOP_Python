from quiz_brain import QuizChecker
from data import question_prompts
from data import correct_answers
from question_model import Question

ques_answ=[]

for i in range(0,len(question_prompts)):
    ques_answ.append(Question(question_prompts[i],correct_answers[i]))

quiz = QuizChecker()
quiz.run_check(ques_answ)

