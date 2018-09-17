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
from string import maketrans
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#table = str.maketrans('', '', string.punctuation)


stop_words = set(stopwords.words('english'))
documents=[]
tokens=[]
doc1=[]
words=[]
vocab=[]
temp=[]
filtered_vocab=[]
with open('CS-AI.csv') as csv_file:
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

#filtered_vocab=list(set(filtered_vocab))

#print(filtered_vocab)
print(len(filtered_vocab))
#print(len(vocab))
#print(documents)





tokens=[]
doc2=[]
words=[]
vocab=[]
temp=[]
##filtered_vocab=[]
with open('CS-DS.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line1 in csv_reader:
        for field1 in line1:
            tokens = word_tokenize(field1)
            #print(tokens)
            doc2.extend(tokens)
        doc2=[w.lower() for w in doc2 if w.isalpha()]#print(doc)
        documents.append(doc2)
        words=[w1.lower() for w1 in doc2 if w1.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc2=[]
        words=[]
for w2 in vocab:
    if w2 not in stop_words:
        filtered_vocab.append(w2)

#filtered_vocab=list(set(filtered_vocab))
print(len(filtered_vocab))






tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
##filtered_vocab=[]
with open('CS-GR.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line2 in csv_reader:
        for field2 in line2:
            tokens = word_tokenize(field2)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w3.lower() for w3 in doc if w3.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w4 in vocab:
    if w4 not in stop_words:
        filtered_vocab.append(w4)

#filtered_vocab=list(set(filtered_vocab))
print(len(filtered_vocab))

tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
#filtered_vocab=[]
with open('CS-IR.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line3 in csv_reader:
        for field3 in line3:
            tokens = word_tokenize(field3)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w5.lower() for w5 in doc if w5.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w6 in vocab:
    if w6 not in stop_words:
        filtered_vocab.append(w6)

#filtered_vocab=list(set(filtered_vocab))

print(len(filtered_vocab))


tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
#filtered_vocab=[]
with open('CS-LG.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line4 in csv_reader:
        for field4 in line4:
            tokens = word_tokenize(field4)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w7.lower() for w7 in doc if w7.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w8 in vocab:
    if w8 not in stop_words:
        filtered_vocab.append(w8)

#filtered_vocab=list(set(filtered_vocab))

print(len(filtered_vocab))

'''
tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
#filtered_vocab=[]
reload(sys)
sys.setdefaultencoding('utf8')

with open('Phy-astro.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line5 in csv_reader:
        for field5 in line5:
            tokens = word_tokenize(field5)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w9.lower() for w9 in doc if w9.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w10 in vocab:
    if w10 not in stop_words:
        filtered_vocab.append(w10)

#filtered_vocab=list(set(filtered_vocab))

print(len(filtered_vocab))
'''


tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
#filtered_vocab=[]
with open('Phy-cond-mat.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line6 in csv_reader:
        for field6 in line6:
            tokens = word_tokenize(field6)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w11.lower() for w11 in doc if w11.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w12 in vocab:
    if w12 not in stop_words:
        filtered_vocab.append(w12)

#filtered_vocab=list(set(filtered_vocab))
print(len(filtered_vocab))



tokens=[]
doc=[]
words=[]
vocab=[]
temp=[]
#filtered_vocab=[]
with open('Phy-gr-qc.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    #line_count = 0
    for line7 in csv_reader:
        for field7 in line7:
            tokens = word_tokenize(field7)
            #print(tokens)
            doc.extend(tokens)
        doc=[w.lower() for w in doc if w.isalpha()]#print(doc)
        documents.append(doc)
        words=[w13.lower() for w13 in doc if w13.isalpha()]
        #print(words) 
        temp=sorted(set(words))
        vocab.extend(temp)
        temp=[]  
        doc=[]
        words=[]
for w14 in vocab:
    if w14 not in stop_words:
        filtered_vocab.append(w14)

filtered_vocab=list(set(filtered_vocab))



#print(filtered_vocab)
print(len(filtered_vocab))

print(documents)
print(len(documents))
