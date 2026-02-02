# Topic of the Day: Sentiment Analysis (VADER)
#
# Explanation: How do you know if a tweet is happy or angry? VADER (Valence Aware Dictionary and sEntiment Reasoner) is a pre-built model in NLTK specifically for social media text.
#
# It understands capitalization ("GREAT" is happier than "great") and emojis.

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Setup (Run once)
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

texts = [
    "I love this product! It's amazing! :D",
    "This is the worst service ever.",
    "It was okay, nothing special."
]

for text in texts:
    scores = sia.polarity_scores(text)
    # Compound score ranges from -1 (Negative) to +1 (Positive)
    print(f"Text: {text}")
    print(f"Score: {scores['compound']}")
    print("---")

# Output:
# Love -> Score close to +0.8
# Worst -> Score close to -0.6
# Okay -> Score close to 0.0