"""
Prog:triviagame.py
Name:Dimitrios Syrbopoulos
Date:08/05/18
Desc:a program that asks questions to the user
"""

def answers():
    print('answers')
#saying hello and welcome to the user and getting user to respond.
response = input ('Hello')
if response == ' Hello' or 'Hi':
    #create a veriable called score to keep track of the users score.
    score = 0
    #list questions and answers.
    question = ['How many legs do spiders have?', 'Whats the capital of China?', 'How big is simons nose?', 'What year was Australia federated?', 'what animal has the scientific name pinguinus impennis?', 'How many stings does a guitar?']
    answers = ['8', 'BeiJing', '17km', '1901', 'Great Auk', '6']
    #updates amount of questions.
    total = len(question)
    #print welcome message and say how many questions are in there.
    print ('welcome to the trivia quiz. There are ', total, ' questions')
    #goes through questions and answers, says if you are wrong or right and gives you a plus one score if right.
    for i, item in enumerate(question):
        print(item)
        guess=input('answers:')
        if guess==answers[i]:
            print('Correct!!!!!!!!!!!!!!!!!!!!')
            score += 1
        else:
            print('Incorrect!?!?!?!')
            print('Correct Answer is:'+answers[i])
    #says that you answered the last question and gives user the score out of amount of questions.
    print('That was the last question, your score is ', score, ' out of ', total)
else:
    print ('bye')




