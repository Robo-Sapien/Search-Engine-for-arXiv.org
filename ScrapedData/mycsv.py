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

#Importing the Cosine Score Class for calculating the ranking
from CosineScore import *

reload(sys)
sys.setdefaultencoding('utf8')

###################### DATA Pre-Processing #########################
class DataPreprocessor:

	"""Extract data from already scraped web data(stored in .csv files).
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


class DataPreprocessor:

	"""Extract data from already scraped web data(stored in .csv files).
    """
	filtered_vocab=[]
	documents=[]

	def dataHandler(self):
		"""(1) Makes a bag of words(vocabulary) after tokenization, stemming, lemmatization & removal of stop words. (2) Makes a list of lists containing tokenized words of documents.


        :return: list of vocabulary of important words & list of all documents in the corpus
        """


		filtered_vocab=[]
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

		#filtered_vocab=list(set(filtered_vocab))
		#print(filtered_vocab)
		#print(len(filtered_vocab))
		#print(len(vocab))
		#print(documents)

		filtered_vocab=list(set(filtered_vocab))
		self.filtered_vocab=filtered_vocab
		self.documents=documents

###################### TF-IDF PROCESSOR #############################
class TF_IDF:
    '''
    This class will provide the functionality for all the postprocessing
    with the following tasks:
    1. Process/Load the tfidf matrix (or update it)
    2. Process the query
    3. Then finally prove the user with the tfidf vector and the query
        vector as attributed.

    '''

    ################ DATA ATTRIBUTES ######################
    tf_idf_matrix=None
    query_vector=None

   # def __init__(self):


    #def load_the_matrix():

    def process_the_matrix(self,word_bag,doc_word_list):
        '''
        Processing the tf-idf matrix and save it as numpy compressed
        matrix.

        :param word_bag: the unique list of the words which will comprise
                            our dictionary.

        :param doc_word_list: the list of the terms for each of the document
                                in the corpus. list of list.
        '''
        #Hashing the word_bag with index
        word_bag=dict([(word_bag[i],i) for i in range(len(word_bag))])
       # print(word_bag)

        #Creating the tfidf matrix
        size=(len(word_bag),len(doc_word_list))
        tf_idf_matrix=np.zeros(size)

        #Creating the doc frequency dictionary
        idf_dict={}

        #Now filling the tf idf matrix with term frequency and doc frequency
        for doc_num in range(len(doc_word_list)):
            doc_terms=doc_word_list[doc_num]
            for term in doc_terms:
            	#print(term)
                #Getting the term id from the hash map

                try:
                	term_id=word_bag[term];
                except Exception as e:
                	pass


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
        for term_id,doc_list in idf_dict.items():
            idf_vector[term_id]=len(doc_list)
        #Taking the inverse of the
        idf_vector=np.log(len(doc_word_list)/idf_vector)

        #Processing the term_frequency
        tf_idf_matrix=1+np.log(1+tf_idf_matrix)


        #Calculating the final tf idf matrix
        idf_vector_reshaped=np.reshape(idf_vector, (7968,1))
        tf_idf_matrix=tf_idf_matrix*idf_vector_reshaped


        self.tf_idf_matrix=tf_idf_matrix

    def process_the_query(self,word_bag,query_word_list):
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
            term_id=word_bag[term]
            query_vector[term_id]=1;

        self.query_vector=query_vector

############################### HANDLER #################################
if __name__ == '__main__':

    #Creating the Parser and extracting the data do it once only later)
    vocab_obj=DataPreprocessor()
    vocab_obj.dataHandler()

    #Processing the tf idf matrix (do it only once in later stage)
    tfidf_solver=TF_IDF()
    tfidf_solver.process_the_matrix(vocab_obj.filtered_vocab,vocab_obj.documents)
    tfidf_solver.process_the_query(vocab_obj.filtered_vocab,["machine","learning"])

    #Getting the page ranking for the above query
    obj = CosineScore(tfidf_solver.query_vector,tfidf_solver.tf_idf_matrix)

    print(obj.getPages(0,10))

if __name__ == '__main__':
    main()
