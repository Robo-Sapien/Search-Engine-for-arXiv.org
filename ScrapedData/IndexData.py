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
from nltk.stem.porter import PorterStemmer

# reload(sys)
# sys.setdefaultencoding('utf8')
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

###################### DATA Pre-Processing #########################
class IndexData:
    """Extract data from already scraped web data(stored in .csv files).
    """
    filtered_vocab = []
    documents = []
    urlList = []
    titleList=[]

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
                firstLineFlag = 0
                for line in csv_reader:
                    if firstLineFlag == 0:
                        firstLineFlag = 1
                        pass
                    else:
                        columnCount=0
                        for field in line:
                            tokens = word_tokenize(field)
                            columnCount += 1
                            if columnCount == 1:
                                self.titleList.append(field.strip('\n'))
                            if columnCount == 5:
                                self.urlList.append(field)
                            doc1.extend(tokens)
                        #print(doc)
                        doc1=[w.lower() for w in doc1 if (w.isalpha() and w not in stop_words)]
                        doc1=[(wordnet_lemmatizer.lemmatize(w)) for w in doc1]
                        doc1=[porter_stemmer.stem(w) for w in doc1]
                        documents.append(doc1)
                        words=[w.lower() for w in doc1 if (w.isalpha() and w not in stop_words)]
                        words=[(wordnet_lemmatizer.lemmatize(w)) for w in words]
                        words=[porter_stemmer.stem(w) for w in words]
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

        filtered_vocab=list(set(filtered_vocab))
        self.filtered_vocab=filtered_vocab
        self.documents=documents

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
        idf_vector=np.log(len(doc_word_list)/(1+idf_vector))

        #Processing the term_frequency
        tf_idf_matrix=1+np.log(1+tf_idf_matrix)


        #Calculating the final tf idf matrix
        idf_vector_reshaped=np.reshape(idf_vector, (idf_vector.shape[0],1))
        tf_idf_matrix=tf_idf_matrix*idf_vector_reshaped

        np.savez( 'tfidf.npz', matrix=tf_idf_matrix, vocab=self.filtered_vocab, urls=self.urlList, titles=self.titleList )

############################### HANDLER #################################
if __name__ == '__main__':

    #Creating the Parser and extracting the data do it once only later)
    preprocessor = IndexData()
    preprocessor.dataHandler()

    #Processing the tf idf matrix (do it only once in later stage)

    preprocessor.process_the_matrix(preprocessor.filtered_vocab,preprocessor.documents)
