'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#define generate_from_frequencies
def generate_from_frequencies(frequencies, max_font_size=None):
    return
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
polarity = []
subjectivity = []
tweets = []

#Pulls out text from each individual tweet and puts it into a list of tweets
for tweet in tweetData:
    text = tweet["text"]
    tweets.append(text)

#Converts every tweet text into a TextBlob
#Find polarity and subjectivity of every tweet and stores it in a list
for i in tweets:
    tb = TextBlob(i)
    polarScore = tb.polarity
    polarity.append(polarScore)

    subjectScore = tb.subjectivity
    subjectivity.append(subjectScore)

#Find number of tweets in database
numofTweets = len(tweets) + 1

#Find average polarity of all tweets | polarity ranges between [-1.0, 1.0]
polarityScore = 0
for i in polarity:
    polarityScore += i
avgPolarity = polarityScore / numofTweets
print("The average polarity is: "+str(avgPolarity))

#Find average subjectivity of all tweets | subjectivity ranges between [0, 1.0]
subjectivityScore = 0
for i in subjectivity:
    subjectivityScore += i
avgSubjectivity = subjectivityScore / numofTweets
print("The average subjectivity is: "+str(avgSubjectivity))

#Create histogram of polarity data
plt.hist(polarity, bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1])
plt.xlabel("Polarity")
plt.ylabel("Number of tweets")
plt.title("Tweet Polarity")
plt.axis([-1.0, 1.0, 0, 65])
plt.grid(True)
plt.show()

#Create histogram of subjectivity data
plt.hist(subjectivity, bins = [0, 0.25, 0.5, 0.75, 1])
plt.xlabel("Subjectivity")
plt.ylabel("Number of tweets")
plt.title("Tweet Subjectivity")
plt.axis([0, 1.0, 0, 45])
plt.grid(True)
plt.show()

#Create scatterplot of data
plt.scatter(polarity, subjectivity)
plt.title("Scatterplot")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.show()

#Create wordcloud
#Combine all tweets into one long string
bigTweet = ""
bigTweet = bigTweet.join(tweets)

#Creates textblob of the big string
allWords = TextBlob(bigTweet)

#Filter words from text blob
filteredWords = {}
commonWords = ["I", "am", "is", "The", "be", "and", "are", "or", "you", "she", "he", "they", "it", "him", "https", "about", "can", "the", "your", "got", "for"]

#Create list of words
wordList = allWords.words

#Filters
for word in wordList:
    if word in commonWords:
        continue
    elif len(word) < 3:
        continue
    elif word.isalpha() == False:
        continue
    else:
        filteredWords[word.lower()] = allWords.word_counts[word.lower()]

wordcloud = WordCloud().generate_from_frequencies(filteredWords)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
