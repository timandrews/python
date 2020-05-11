#!/usr/bin/env python3.8
file_name = input("Enter your file:  ")
input_file = open(file_name, 'r')

for line in input_file:
    line = line.strip('\n')
    print(line)
    print("The line is " , len(line), " characters long.")
    
    if 'o' in line:
        print('There is an "o" in the name')
        
    print("++++++++++")


input_file.close()