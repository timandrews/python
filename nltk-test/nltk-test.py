
import nltk
# nltk.download()

# create token from a random string
from nltk.tokenize import sent_tokenize, word_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))

# Extract content from a random webpage
import urllib.request
response =  urllib.request.urlopen('http://www.gutenberg.org/files/10/10-h/10-h.htm')
html = response.read()
print(html)

# strip out all HTML tags from the webpage content
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

# tokenize text from the
tokens = [t for t in text.split()]
print(tokens)

# plot the frequency of words
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):

        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)