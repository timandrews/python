from fuzzywuzzy import fuzz
from fuzzywuzzy import process

string1 = 'some string'
string2 = 'another string'
string3 = 'still another string'

print('string1 ="'+ string1+'"')
print('string2 ="'+ string2+'"')
print('string3 ="'+ string3+'"')
print('The difference between string1 and string2 is:', fuzz.ratio(string1, string2))
print('The difference between string2 and string1 is:', fuzz.ratio(string2, string3))
print('The difference between string2 and string 3 is:  ', fuzz.ratio(string2, string3))

print('The partial difference between string1 and string2 is:', fuzz.partial_ratio(string1, string2))
print('The partial difference between string2 and string1 is:', fuzz.partial_ratio(string2, string3))
print('The partial difference between string2 and string 3 is:  ', fuzz.partial_ratio(string2, string3))

print('Example 2 from datacamp.com:  ')
Str1 = "The supreme court case of Nixon vs The United States"
Str2 = "Nixon v. United States"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
Token_Set_Ratio = fuzz.token_set_ratio(Str1,Str2)
print('simple ratio', Ratio)
print('partial ratio', Partial_Ratio)
print('sorted token ratio', Token_Sort_Ratio)
print('set token ratio', Token_Set_Ratio)

print('Example 3 for process module:  ')
str2Match = "apple inc"
strOptions = ["Apple Inc.","apple park","apple incorporated","iphone"]
Ratios = process.extract(str2Match,strOptions)
print(Ratios)
# You can also select the string with the highest matching percentage
highest = process.extractOne(str2Match,strOptions)
print(highest)