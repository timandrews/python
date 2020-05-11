#!/usr/bin/env python3.8
def modifyString(input_file, output_file, char_to_remove):
    EMPTY_STRING =''
    
    output =""
    
    tmp_num_total_chars = 0
    tmp_num_removals = 0

    for line in input_file:
        orig_line_length = len(line) - 1
        tmp_num_total_chars = tmp_num_total_chars + orig_line_length
        
        modified_line = line.replace(char_to_remove.lower(), EMPTY_STRING).replace(char_to_remove.upper(),EMPTY_STRING)
        tmp_num_removals = tmp_num_removals + (orig_line_length - (len(modified_line) - 1))
        
        print(modified_line.strip('\n'))
        output_file.write(modified_line)
    
    return (tmp_num_total_chars, tmp_num_removals)


print ("This program will display the contents of a provided text file with all occuraences of the letter 'e' removed."
       )
file_name = input("Enter file name (including file extension): ")
input_file = open(file_name, 'r')

char_to_remove = input("Which character would you like to remove?  ")

new_file_name = 'e_' + file_name
output_file = open(new_file_name , 'w')

num_total_chars, num_removals = modifyString(input_file, output_file, char_to_remove)

input_file.close()
output_file.close()

print(num_removals, "occurences of the letter 'e' removed")
print('Percentage of data lost: ', int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file: ', new_file_name)