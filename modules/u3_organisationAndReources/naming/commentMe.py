"""
Prog: commentMe.py
Name: Dimitrios Syrbopoulos
Date: 18/04/18
Desc: a calculator that determis the perimeter of a circle
"""
#print welcome message
print('Welcome to the Circle Calculator!')
#make user input radius
r = input('Enter a radius: ')
r = int(r)
#calculate area and print it
area = 3.14 * r * r
print('The area is', area)
#calculate perimeter and print it
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
