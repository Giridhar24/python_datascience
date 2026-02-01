# Topic of the Day: Word Clouds
#
# Explanation: Yesterday we cleaned text.
#
# Today we visualize it.
#
# A Word Cloud makes frequent words appear larger.
#
# It is the quickest way to see "What is this text about?"

# pip install wordcloud matplotlib
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python is amazing. Data Science is fun. Python Python Python code."

# 1. Generate Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 2. Display
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") # Hide X/Y axis numbers
plt.show()