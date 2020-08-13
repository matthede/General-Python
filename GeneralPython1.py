# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:21:57 2020

@author: matth
"""

################### Python Data Types #####################

int_ = 1

float_ = 10.0

complex_ = 1 + 2j

string = 'Hi there!  This is a string.'

data_types = [int_, float_, complex_, string]

for dt in data_types:
    print('{} is a {}'.format(str(dt), str(type(dt))))
    
######### Logical and Math Operators with Examples ########
    
# Logical
    
x = 10

y = 5

x > y 

x < y

x != y

x == x

y >= y

y <= y

# Math

add = x + y

subtract = x - y

multiply = x * y

divide = x / y

floor_division = x // y 

moduolo = x % (y + 1)

exponents = x ** x

print(add)


############## Python Data Structures #####################

# lists
# the list data structure is a mutable collection of data
# mutable means it can be changed
# Items in a list can be accessed by their index

numbers = [n for n in range(100)]

print(numbers)

numbers.append(100)

print(numbers)

numbers.remove(0)

print(numbers)

numbers[1]

numbers[0:10]

numbers[-1]

# Tuples
# the tuple data structure is an immutable collection of data
# immutable means it can't be changed

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup)

# Sets
# sets are mutable collection of unique data

set_ = {1, 2, 3, 4, 5} 

set__ = {1, 2, 3, 4, 5, 5}

print(set__)

# Dictionaries
# nA unordered collection of key value paired data

teams = {
        "Bills": ["Josh Allien", "Tredavious White"],
        "Jets": ["Sam Darnold", "CJ Mosley"],
        "Patriots": ["Cam Newton", "Julian Edelman"]
        }

teams.keys()

teams.values()

teams.items()

