"""
Prog:triviagame.py
Name:Dimitrios Syrbopoulos
Date:08/05/18
Desc:a program that asks questions to the user
"""
def answers():
    print('answers')
response = input ('Hello')
if response == ' Hello':
    print ('welcome to the trivia quiz')
else:
    print ('bye')

question = ['How many legs do spiders have?', 'Whats the capital of China?', 'How big is simons nose?', 'What year was Australia federated?', 'what animal has the scientific name pinguinus impennis?']
answers = ['8', 'BeiJing', '17km', '1901', 'Great Auk']
for i, item in enumerate(question):
    print(item)
    input('answers:')
    print(answers[i])


