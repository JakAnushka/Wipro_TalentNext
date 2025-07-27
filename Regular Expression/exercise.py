'''1. Write a program to find check if a string has only octal digits. Given string

['789', '123', '004']'''
strings = ['789', '123', '004']
octals = [s for s in strings if all(ch in '01234567' for ch in s)]
print("Octal strings:", octals)

'''2. Extract the user id, domain name and suffix from the following email addresses.

emails """zuck@facebook.com

sunder33@google.com

jeff42@amazon.com""". '''
import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

result = re.findall(r'(\w+)@(\w+)\.(\w+)', emails)
print("Email info:", result)


'''3. Split the following irregular sentence into proper words

sentence = """A, very very; irregular_sentence""" ## expected outout: A very

very irregular sentence.'''
import re

sentence = "A, very very; irregular_sentence"
cleaned = re.sub(r'[^\w\s]', '', sentence.replace('_', ' '))
print("Clean sentence:", cleaned)


'''4. Clean up the following tweet so that it contains only the user's message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

#tweet = Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@pxOd cc: @garybernhardt #rstats***

##desired output = 'Good advice What I would do differently if I was learning to code

today.'''
import re

tweet = """Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej@pxOd cc: @garybernhardt #rstats***"""

cleaned_tweet = re.sub(r"(RT|cc:?)|(@\w+)|(#\w+)|http\S+|[^\w\s]", "", tweet)
print("Cleaned tweet:", cleaned_tweet.strip())


'''5. Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

Code to retrieve the HTML page is given below:

import requests
r=requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html") r.text # html text is contained here

desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 'This is a another paragraph!", "This is a new sentence without a paragraph break, in bold italics.']'''
import requests
from bs4 import BeautifulSoup

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
soup = BeautifulSoup(r.text, 'html.parser')

texts = [tag.get_text() for tag in soup.find_all()]
print("Extracted text:", texts)

'''6. Given below list of words, identify the words that begin and end with the same character.

civic

trust

widows

maximum

museums

aa

as
'''
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matches = [word for word in words if word[0] == word[-1]]
print("Matching words:", matches)
