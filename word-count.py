#!/usr/bin/env python3


def  getFile():
    
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name:  ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print('Input file not found - please reenter:  ')
            
    return (file_name, input_file)

def countWords(input_file, search_word):
    
    space = ' '
    num_occurrences = 0
    word_delimiters = (space, ',', ';', ':', '.', '\n', '"', "'", '(' , ')')

    search_word_len = len(search_word)
    
    for line in input_file:
        end_of_line = False
        
        line = line.lower()
        
        while not end_of_line:
                try:
                    index = line.index(search_word)
                    
                    if index == 0 and line[search_word_len] in word_delimiters:
                        found_search_word = True
                    elif line [index - 1] in word_delimiters and line[index + search_word_len] in word_delimiters:
                        found_search_word = True
                    else:
                        found_search_word = False
                        
                    if found_search_word :
                        num_occurrences = num_occurrences + 1
                    
                    line = line[index + search_word_len : len(line)]
                except ValueError:
                    end_of_line = True
                    
    return num_occurrences


print('This program will display the number of occurrences of a')
print('specified word within a given text file\n')

file_name, input_file = getFile()

search_word = input('Enter word to search')
search_word = search_word.lower()

num_occurrences = countWords(input_file, search_word)

if num_occurrences == 0 :
    print('No occurrences of word,', '"' + search_word + '"', 'found in file', file_name)
else :
    print('The word', '"' + search_word + '"', 'occurs', num_occurrences, 'times in file', file_name)