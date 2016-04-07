"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
#imports all the functions from arithmetic
from arithmetic import *

# Your code goes here

while True:
    user_input = raw_input()
    our_tokens = user_input.split(" ")

    if our_tokens[0] == 'q':
         break
    elif our_tokens[0] == '+':
        print add(int(our_tokens[1]), int(our_tokens[2]))
    elif our_tokens[0] == '-':
        print subtract(int(our_tokens[1]), int(our_tokens[2]))
    elif our_tokens[0] == '*':
        print multiply(int(our_tokens[1]), int(our_tokens[2]))
    elif our_tokens[0] == '/':
        print divide(int(our_tokens[1]), int(our_tokens[2]))
    elif our_tokens[0] == 'square':
        print square(int(our_tokens[1]))
    elif our_tokens[0] == 'cube':
        print cube(int(our_tokens[1]))
    elif our_tokens[0] == 'pow':
        print power(int(our_tokens[1]), int(our_tokens[2]))
    elif our_tokens[0] == 'mod':
        print mod(int(our_tokens[1]), int(our_tokens[2]))
    else:
        print "Error"