# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:21:07 2020

@author: matth
"""

import random
import numpy as np
import itertools

############### Python Conditional Statements #############

x = 15

if x > 10:
    print('x is greater than 10!')
    
x = 9
    
if x > 10:
    print('x is greater than x!')
else:
    print('x is than 10!')

if x > 10:
    print('x is greater than 10!')
elif x > 5:
    print('x is greater than 5!')
else:
    print('Less than x!')
    
# These are very basic examples.  
# You can also use 'and' or 'or' in your statements

x = 12

if (x >= 10) and (x <= 15):
    print('Between 10 and 15.')
else:
    print('Smaller than 10 or larger than 15.')
    
x = 7

if (x > 10) or (x % 2 != 0):
    print('X is greater than 10 or not even.')
else:
    print('X is less than 10 or even.')
    
# What if you want to nest an if statement?
    
random_ = random.randint(0, 1000)

RANDOM = True


if RANDOM:
    if random_ % 2 == 0:
        print('Random and even')
    else:
        print('Random and not even')
else:
    if x >= 100:
        if x % 2 == 0:
            print('even')
        else:
            print('not even')
    else:
        print('less than 100.')
        
##################### Python Loops ########################
        
# Two main types of loops in Python, for and while
        
x =  [n for n in range(1, 101)]

# Looping through a list

for n in x:
    print(n)
    
for n in x:
    if n % 2 == 0:
        print(n)
    else:
        print('Odd')
        
        
# List comprehension is the most efficient way to loop through 
# a list if it's 
        
[n for n in x]

[n for n in x if n % 2 == 0]

[n if n % 2 == 0 else 'Odd' for n in x]

# What if you want to loop through two lists?

listone = [random.randint(0, 100) for n in range (10)]

listtwo = [random.randint(0, 100) for n in range (10)]

listthree = []

for o, t in zip(listone, listtwo):
    if (o % 2 == 0) and (t % 2 == 0):
        listthree.append(listone.index(o))

# What if your lists aren't the exact same length?
        
listone = [random.randint(0, 100) for n in range (10)]

listtwo = [random.randint(0, 100) for n in range (15)]

listthree = []

for o, t in itertools.zip_longest(listone, listtwo, fillvalue = 0):
    print(o, t)

# You can also loop through sets, tuples, and arrays
# Looping through a dictionary
    
teams = {
        "Bills": ["Josh Allien", "Tredavious White"],
        "Jets": ["Sam Darnold", "CJ Mosley"],
        "Patriots": ["Cam Newton", "Julian Edelman"]
        }

for k in teams.keys():
    print(k)
    
for v in teams.values():
    print(v)
    
for k, v in teams.items():
    if k == 'Bills':
        print(v)
        
# While loops run while a condition is true
        
count = 0

while count < 10:
    count += 1
    print(count)


odd = True

while odd:
    ran = random.randint(0, 100)
    if ran % 2 == 0 and ran < 50:
        odd = False
    else:
        print(ran)
        
        
#################### Error Handling #######################
     
# Try lets you attempt a block of code
# If there's an error, another block of code can run in the 'except' portion
        
y = 't'
        
try:
    divide = 6 / y
except:
    print('y is not a number.')

    
y = 4

try:
    divide = 6 / y
except:
    print('y is not a number.')
else:
    print('The output of divide is {}'.format(str(divide)))
    
try:
    divide = 6 / y
except:
    print('y is not a number.')
else:
    print('The output of divide is {}'.format(str(divide)))
finally:
    print('The error handling example is finished.')
    
# assert lets you test if a condition is true, if it isn't 
# then an assertion error will be raised
    
number = random.randint(0, 100)

assert number < 50, 'The number is higher than 50.'

print(number)


###################### Functions ##########################

# A function is a block of code that runs when called and can take input when 
# it's called or just process code without input

def hello():
    print('Hello!')
    
def hello_(name):
    print('Hello {}!'.format(name))
    
hello()

hello_('Dave')

# Functions can print outputs, but can also return them to an object

def square(side):
    return side * side
    
area = square(5)

print(area)

def euro_dollar(euro):
    # this function converts euro to dollar based on 8/17/2020 exchange rate
    return '${}'.format(str(round(euro * 1.18710, 2)))

euro_dollar(500)

# You can input data types to functions as well as collections

def list_metrics(l):
    print('Max: {}, Min: {}, Total: {})'.format(str(max(l)), str(min(l)), str(sum(l))))
    
l = [n for n in range(1, 101)]

list_metrics(l)
