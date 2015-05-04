"""
Regular Expressions Exercise
----------------------------

Write a regular expression that can match the number and type of traveller
from strings like the following::
    
    "5 men, 7 dogs and 12 goats are travelling together."
    
    "3 elephants and 1 lion are travelling together."
    
    "2 women, 5 children, 7 horses and 2 cats are travelling together."

You can assume that each clause consists of an integer followed by
one word that describes the type.

"""

import re

# we are looking for one or more digits followed by space, followed by a word
pattern = re.compile(r'(\d+)\s+(\w+)')

test1 = "5 men, 7 dogs and 12 goats are travelling together."
print test1
for number, type in pattern.findall(test1):
    print number, type

test2 = "3 elephants and 1 lion are travelling together."
print test2
for number, type in pattern.findall(test2):
    print number, type

test3 = "2 women, 5 children, 7 horses and 2 cats are travelling together."
print test3
for number, type in pattern.findall(test3):
    print number, type
