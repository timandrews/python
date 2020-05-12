from fuzzywuzzy import fuzz
from fuzzywuzzy import process

string1 = 'some string'
string2 = 'another string'
string3 = 'still another string'

print('The difference between ', string1, ' and ', string2, ' is:  ', fuzz.ratio(string1, string2))