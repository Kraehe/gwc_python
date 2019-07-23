'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

twt_txt = ""
pos_txt = ""
neg_txt = ""
# loops through each tweet to add tweet text to the polarity and subjectivity lists
for tweet in tweetData:
    tb = TextBlob(tweet["text"])
    if tb.polarity == 0:
        twt_txt += tweet["text"] # creates the tweet text variable and adds the text of each tweet to itself
    elif tb.polarity > 0:
        pos_txt += tweet["text"]
    elif tb.polarity < 0:
        neg_txt += tweet["text"]
    else:
        continue

def wCloud(txt):
    twt_blob = TextBlob(txt)
    blob = {}
    for word in twt_blob.words:
        if len(word) > 3:
            if word == 'about' or word == 'http' or word == 'https' or word == 'your':
                continue
            elif word.isalpha() == False:
                continue
            else:
                count = twt_blob.word_counts[word.lower()]
                blob[word.lower()] = count
        else:
            continue
    wordcloud = WordCloud().generate_from_frequencies(blob)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


wCloud(twt_txt)
wCloud(pos_txt)
wCloud(neg_txt)

# Textblob sample:
# print("avg polarity: ", sum(polarity) / len(polarity))
# print("avg subjectivity: ", sum(subjectivity) / len(subjectivity))

# makes a histogram of the polarity of each tweet
# num_bin1 = len(polarity)
# n, bins, patches = plt.hist(polarity, num_bin1, facecolor='red', alpha=0.5)
# plt.show()
#
# # makes a histogram of the subjectivity of each tweet
# num_bin2 = len(subjectivity)
# n, bins, patches = plt.hist(subjectivity, num_bin2, facecolor='blue', alpha=0.5)
# plt.show()
# area = len(polarity)+len(subjectivity)  # 0 to 15 point radii
# plt.scatter(polarity, subjectivity, s=area, c=subjectivity, alpha=0.5)
# plt.show()
