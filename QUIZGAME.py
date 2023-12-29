print("**********************")
print("WELCOME TO THE ULTIMATE OOPS QUIZ GAME")


question_bank=[

{"text":"The ability of one to acquire methods and attributes of another class is called?","answer":"A"},

{"text":"which of the following is type of inheritence?","answer":"D"},

{"text":"what type of inheritence has  multiple subclasses to a single super class?","answer":"C"},
{"text":"what is the depth of multilevel inheritence in python?","answer":"A"},
{"text":"what does?","answer":"B"},

]

options= [

["A. Inheritance ","B.Abstraction ","C.Polymorphism ","D.Objects "],
["A. Single ","B.Double ","C.Multiple ","D.BOTH A & C "],
["A. Multiple Inheritance","B.Multilevel Inheritence","C.Hierarchical Inheritence","D.None Of These"],
["A. Two level","B.Three level","C.Any Level","D.None Of These"],
["A. Method Recursive Object ","B.Method Resolution Order","C.Main Resolution Order","D.Method Resolution Object"],





]

score=0

def check_answer(user_guess,correct_answer):

  if user_guess == correct_answer:
     
     return True
  
  else :
     return False
  

for question_num in range(len(question_bank)):
     
     print("\n")
     print("***********************")
     print(question_bank[question_num]["text"])
     for i in options[question_num]:
        print(i)

     
     
     guess=input("Enter your answer (A/B/C/D): ").upper()
     is_correct=check_answer(guess,question_bank[question_num]["answer"])
     if is_correct:
           print("correct answer")
           score+=1
     else:
           print("incorrect Answer")
           print(f"The correct answer is {question_bank[question_num]['answer']}")
     print(f"Your current score is{score}/{question_num+1}")

print("\n \n")
print(f"you have given {score} correct answer")
print(f"your score is {(score/len(question_bank))*100}%")         



