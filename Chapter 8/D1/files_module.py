#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
""" This module contains functions to open and read a file for the main part of the program.
"""

def open_file():
    file_opened = False
    num_tries_remaining = 3
    while (not file_opened) and (num_tries_remaining > 0):
        try:
            file_name = input('Enter name of file:  ')
            input_file = open(file_name, 'r')
            file_opened = True
        except IOError:
            num_tries_remaining = num_tries_remaining -1
            print('Error opening file:  ', ' - please try again')
            

            

    
