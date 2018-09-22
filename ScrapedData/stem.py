from __future__ import print_function
import csv
import numpy as np
import nltk
from nltk import word_tokenize
from nltk import FreqDist
from nltk.stem import WordNetLemmatizer
import pandas
from nltk.corpus import stopwords
import string
# from string import maketrans
import sys
from scipy import spatial
import numpy
from nltk.stem.porter import PorterStemmer

reload(sys)
sys.setdefaultencoding('utf8')
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()


filtered_vocab=[]
filtered_vocab_stemmed=[]
filtered_vocab_lemmatized=[]
filtered_vocab_lemmatized_stemmed=[]
documents=[]
stop_words = set(stopwords.words('english'))
file_list=['CS-AI.csv','CS-DS.csv','CS-GR.csv','CS-IR.csv','CS-LG.csv','Phy-cond-mat.csv','Phy-gr-qc.csv']

for filename in file_list:
	tokens=[]
	doc1=[]
	words=[]
	vocab=[]
	temp=[]
	with open(filename) as csv_file:
	    csv_reader = csv.reader(csv_file)
	    #line_count = 0
	    for line in csv_reader:
	        for field in line:
	            tokens = word_tokenize(field)
	            #print(tokens)
	            doc1.extend(tokens)
		    #print(doc)
		    doc1=[w.lower() for w in doc1 if w.isalpha()]
		    documents.append(doc1)
		    words=[w.lower() for w in doc1 if w.isalpha()]
		    #words=[w.lower() for w in doc]
		    #words = [w.translate(table) for w in doc]
		    #print(words)
		    temp=sorted(set(words))
		    vocab.extend(temp)
		    temp=[]
		    doc1=[]
		    words=[]
	for w in vocab:
	    if w not in stop_words:
	        filtered_vocab.append(w)

for w in filtered_vocab:
	filtered_vocab_stemmed.append(porter_stemmer.stem(w))

for w in filtered_vocab:
	filtered_vocab_lemmatized.append(wordnet_lemmatizer.lemmatize(w))

for w in filtered_vocab_lemmatized:
	filtered_vocab_lemmatized_stemmed.append(porter_stemmer.stem(w))


filtered_vocab=list(set(filtered_vocab))
filtered_vocab_stemmed=list(set(filtered_vocab_stemmed))
filtered_vocab_lemmatized=list(set(filtered_vocab_lemmatized))
filtered_vocab_lemmatized_stemmed=list(set(filtered_vocab_lemmatized_stemmed))
#print(filtered_vocab_stemmed)
#print(filtered_vocab_lemmatized)
print(filtered_vocab_lemmatized_stemmed)
print(len(filtered_vocab_lemmatized_stemmed))
print(len(filtered_vocab_lemmatized))
print(len(filtered_vocab))
print(len(filtered_vocab_stemmed))