#!/usr/bin/python3

'''
The following Python program generates all the possible spellings of the last 4 digits of any
given phone number.  This is usually refered to a a phoneword

See https://en.wikipedia.org/wiki/Phoneword

The program utilizes the following programming features:
dictionaries
''' 



def getPhoneNum():
    valid_phone_num = False
    empty_str = ''
    
    while not valid_phone_num:
        phone_num = input('Enter a phone number:  ')
        
        if len(phone_num) != 12 or phone_num[3] != '-' or phone_num[7] != '-':
            print('Phone number is invalid. Please retype')
        else:
            k = 0
            valid_phone_num = True
            phone_num_digits = phone_num.replace('-', empty_str)
            
            while valid_phone_num and k < len(phone_num_digits):
                if not phone_num_digits[k].isdigit():
                    print('Invalid character, must be a digit')
                    valid_phone_num = False
                else:
                    k = k + 1
    return phone_num

def displayAllSpellings(phone_num):
    translate = {'0':('0'), 
                 '1':('1'),
                 '2':('a','b','c'), 
                 '3':('d','e','f'), 
                 '4':('g','h','i'), 
                 '5':('j','k','l'), 
                 '6':('m','n','o'), 
                 '7':('p','q','r','s'), 
                 '8':('t','u','v'), 
                 '9':('w','x','y','z')}
    
    print(phone_num)
    
    for letter1 in translate[phone_num[8]]:
        for letter2 in translate[phone_num[9]]:
            for letter3 in translate[phone_num[10]]:
                for letter4 in translate[phone_num[11]]:
                    print(phone_num[0:8] + letter1 + letter2 + letter3 + letter4)

if __name__ =='__main__':
    print('The program will generate all possible spellings of the last 4 digits of any phone number.')
    
    terminate = False
    
    while not terminate:
        phone_num = getPhoneNum()
        displayAllSpellings(phone_num)
        
        response = input('Enter another number?  ')
        if response == 'n':
            terminate = True