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

from scipy import spatial
import numpy


class CosineScore:
    """Calculate cosine similarity score for each document and rank them

    :param query: query vector

    :param matrix: tf-idf numpy matrix
    """
    rank = []
    docIndex = []
    score = []
    def __init__(self, query, matrix):
        """Constructor which calculates cosine similarity score for each document"""
        for j in range(matrix.shape[1]):
            column = matrix[:,j]
            self.docIndex.append(j)
            self.score.append(1 - spatial.distance.cosine(column, query))
        self.rank = list(reversed([x for _, x in sorted(zip(self.score, self.docIndex))]))

    def getPages(self,start,end):
        """To get the indices of the douments between the given ranks

        :param start: starting *rank*.

        :param end: rank after the last rank.

        :return: list of document indices for ranks from start to end-1.
        """
        return self.rank[start:end]



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



class TF_IDF:
    '''
    This class will provide the functionality for all the postprocessing

    '''

    ################ DATA ATTRIBUTES ######################
    tf_idf_matrix=None
    query_vector=None

    def __init__(self):


    def load_the_matrix():

    def process_the_matrix(word_bag,doc_word_list):
        '''
        Processing the tf-idf matrix and save it as numpy compressed
        matrix.
        '''
        #Hashing the word_bag with index
        word_bag=dict([(word_bag[i],i) for i in range(len(word_bag))])

        #Creating the tfidf matrix
        size=(len(word_bag),len(doc_word_list))
        tf_idf_matrix=np.zeros(size)

        #Creating the doc frequency dictionary
        idf_dict={}

        #Now filling the tf idf matrix with term frequency and doc frequency
        for doc_num in range(len(doc_word_list)):
            doc_terms=doc_word_list[doc_num]
            for term in doc_terms:
                #Getting the term id from the hash map
                term_id=word_bag[term];

                #Adding the contribution of this term of the doc frequency
                if term_id not in idf_dict.keys():
                    idf_dict[term_id]=[doc_num]
                elif doc_num not in idf_dict[term_id]:
                    idf_dict[term_id].append(doc_num)

                #Adding the word count to the tf_idc matrix to keep the frequency track
                tf_idf_matrix[term_id,doc_num]+=1


        #Now we are done with the term frequency and doc frequency
        #Processing the idf vector
        idf_vector=np.zeros(len(word_bag))
        for term_id,doc_list in idf_dict:
            idf_vector[term_id]=len(doc_list)
        #Taking the inverse of the
        idf_vector=np.log(len(doc_word_list)/idf_vector)

        #Processing the term_frequency
        tf_idf_matrix=1+np.log(1+tf_idf_matrix)


        #Calculating the final tf idf matrix
        tf_idf_matrix=tf_idf_matrix*idf_vector

        self.tf_idf_matrix=tf_idf_matrix

    def process_the_query(self,word_bag,query_word_list):
        '''

        '''
        #Hashing the word_bag with index
        word_bag=dict([(word_bag[i],i) for i in range(len(word_bag))])

        #Creating the query vector
        query_vector=np.zeros((len(word_bag),1))

        #Iterating through the query
        for term in query_word_list:
            term_id=word_bag[term]
            query_vector[term_id]=1;

        self.query_vector=query_vector

def main():
    # query = [0, 1, 0]
    # matrix = numpy.array([[2, 1, 3], [4, 3, 5], [6, 5, 7]])

    tfidf_solver=TF_IDF()
    tfidf_solver.process_the_matrix(filtered_vocab,documents)
    tfidf_solver.process_the_query(["learning","machine"])
    #
    obj = CosineScore(tfidf_solver.query_vector,tfidf_solver.tf_idf_matrix)
    print(obj.getPages(0,10))
