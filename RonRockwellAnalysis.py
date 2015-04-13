# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 18:18:52 2015

@author: Stephen Bishop
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import FreqDist
from __future__ import division

storytext = open("ronrockwell.txt").read()

def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)

preprocessedStory = preprocess(storytext)


tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]

def lexical_diversity(text):
    return len(set(text)) / len(text)
     
def percentage(count, total):
    return 100 * count / total

lexical_diversity(tokens)
len(tokens)
len(set(tokens))


# Frequency Distribution
fdist1 = FreqDist(tokens)
print(fdist1)
fdist1.items()[0:10]
fdist1.plot(50, cumulative=True)

from nltk.corpus import stopwords
stop = stopwords.words('english')
remstop = [i for i in tokens if i not in stop]
remstop[0:20]
len(remstop)
len(set(remstop))

# Frequency Distribution with all the garbage removed
fdist2 = FreqDist(remstop)
print(fdist2)
fdist2
fdist2.items()[0:20]
fdist2.plot(50, cumulative=True)

lexical_diversity(remstop)

array = fdist2.items()[0:20]
mylist = [list(i) for i in array]

# write out the top 20 terms to csv file
import csv
with open('newfile.csv', 'wb') as result:
    writer = csv.writer(result, dialect='excel')
    writer.writerows(array)

with open('tokens.csv', 'wb') as result:
    writer = csv.writer(result, dialect='excel')
    writer.writerow(remstop)
    