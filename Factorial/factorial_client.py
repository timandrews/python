from factorial import *
import math

# first using the math.factorial method
print('using import math function:   ')
num = int(input('Enter number to computer factorial of:  '))
valid_input = False

while not valid_input:
    try:
        result = math.factorial(num)
        print(result)
        valid_input = True
    except ValueError:
        print('Cannot compute factorial of negative numbers')
        num = int(input('Enter a number:  '))

# Now to try it my own way to see if I remember
print('Now for my way ')
num = int(input('Enter number to compute factorial of:  '))
valid_input = False
while not valid_input:
    try:
        if num < 0 :
            raise ValueError('Cannot compute factorial of negative numbers')

        print (my_factorial(num))
        valid_input = True
    except ValueError as err_msg:
        print(err_msg)
        num = int(input('Enter a number:  '))