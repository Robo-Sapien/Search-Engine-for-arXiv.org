# from __future__ import print_function
# import csv
import numpy as np
import nltk
from nltk import word_tokenize
# from nltk import FreqDist
from nltk.stem import WordNetLemmatizer
# import pandas
from nltk.corpus import stopwords
import string
# from string import maketrans
import sys
from scipy import spatial
from nltk.stem.porter import PorterStemmer

#Importing the Cosine Score Class for calculating the ranking
from CosineScore import *

###################### TF-IDF PROCESSOR #############################
class SearchQuery:
    '''
    This class will provide the functionality for all the postprocessing
    with the following tasks:
    2. Process the query
    3. Then finally prove the user with the tfidf vector and the query
        vector as attributed.

    '''

    ################ DATA ATTRIBUTES ######################
    queryVector = None
    tfidfMatrix = None
    urlList = None
    titleList = None
    tfidf = None

    def __init__(self):
        self.tfidf = np.load('tfidf.npz')
        self.tfidfMatrix = self.tfidf['matrix']
        self.urlList = self.tfidf['urls']
        self.titleList = self.tfidf['titles']

    def processQuery(self, word_bag, query_word_list):
        '''
        This function will take a query from the user, then make a boolean
        encoding of the query in the space of the word bag.

        :param word_bag: the list of the unique word in our dictionary

        :param query_word_list: the list of the words in the query
        '''

        #Hashing the word_bag with index
        word_bag=dict([(word_bag[i],i) for i in range(len(word_bag))])

        #Creating the query vector
        query_vector=np.zeros((len(word_bag),1))

        #Iterating through the query
        for term in query_word_list:
            try:
                term_id=word_bag[term]
                query_vector[term_id] = 1
            except Exception as e:
                pass

        self.queryVector = query_vector

############################### HANDLER #################################
    def search(self, queryString):

        stop_words = set(stopwords.words('english'))
        porter_stemmer = PorterStemmer()
        wordnet_lemmatizer = WordNetLemmatizer()
        query = word_tokenize(queryString)
        query=[w.lower() for w in query if (w.isalpha() and w not in stop_words)]
        query=[(wordnet_lemmatizer.lemmatize(w)) for w in query]
        query=[porter_stemmer.stem(w) for w in query]

        self.processQuery( self.tfidf['vocab'], query )

        #Getting the page ranking for the above query
        obj = CosineScore(self.queryVector, self.tfidfMatrix)

        rankList = obj.getPages(10)
        finalList = []
        for docIndex in rankList:
            finalList.append((self.titleList[docIndex], self.urlList[docIndex]))
        return finalList
#
# def main():
#     obj = SearchQuery()
#     obj.search('Andy')
#
# if __name__ == '__main__':
#     main()
