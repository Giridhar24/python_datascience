# Topic of the Day: Natural Language Processing (NLP) Basics
#
# Explanation: How do computers understand text? They turn words into numbers.
#
# Tokenization: Splitting a sentence into words.
#
# Stop Words: Removing common, useless words (the, a, is) to focus on the important ones.

# pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Setup (Run once)
nltk.download('punkt')
nltk.download('stopwords')

text = "Data Science is amazing and fun!"

# 1. Tokenize (Split)
tokens = word_tokenize(text)
print(f"Tokens: {tokens}")
# Output: ['Data', 'Science', 'is', 'amazing', 'and', 'fun', '!']

# 2. Remove Stop Words
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words]

print(f"Keywords: {filtered}")
# Output: ['Data', 'Science', 'amazing', 'fun', '!'] ("is" and "and" are gone)