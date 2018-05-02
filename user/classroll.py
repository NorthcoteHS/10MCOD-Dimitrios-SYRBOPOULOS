"""
prog: classroll.py
name: Dimitrios Syrbopoulos
Date: 01/05/2018
Desc: making a roll that tells who is on guinne pig duty
"""
#import random
import random
#the roll is the following names
roll = ['Jessica', 'Emily', 'Jordan', 'Kayley', 'Bruce', 'Michael', 'Everett', 'Lisa', 'Sam', 'Noah']
#created a veriable for the cleaner and it is the third person
cleaner = roll[2]
#display the users name
print('the cleaner is', cleaner )
#enrolment equals the length of the roll
enrolment= len(roll)
#add james
roll.append('james')
#deleting the third person on the roll
del roll[2]
#change Michael to Mike
roll [5] = 'Mike'
#alphabetise the list and reverse it
list.sort(roll)
list.reverse(roll)
#print random name
print(random.choice(roll))
just halves the roll
half1 = roll[0:5]
half2 = roll[6:10]
