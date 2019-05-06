# Python program to generate word vectors using Word2Vec 
  
# importing all necessary modules 
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
import sys
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec 
  

def main():
    '''This takes a sample file and creates a Word2Vec model that gets
    saved into a .bin file for later use'''
    
    FILENAME = sys.argv[1]
    MODELTYPE = 0 #1 for Skip Gram, 0 for CBOW
    OUT_FILE_NAME = sys.argv[2] #should be a .bin file
    SIZE = 100 #size of model
    WINDOW = 5 #window for model


    sample = open(FILENAME, "r", encoding="utf8") 
    s = sample.read() 
    testList = ["in", "this", "the", "it", "a", "and", "as", "have"]
    
    # Replaces escape character with space 
    f = s.replace("\n", " ") 
    
    data = [] 
    
    # iterate through each sentence in the file 
    for i in sent_tokenize(f): 
        temp = [] 
        
        # tokenize the sentence into words 
        for j in word_tokenize(i):
            if j.lower() not in testList: 
                temp.append(j.lower()) 
    
        data.append(temp) 


    # Create model
    model1 = gensim.models.Word2Vec(data, min_count = 1, size = SIZE, window = WINDOW, sg=MODELTYPE) 
    
    #Save model
    model1.wv.save_word2vec_format(OUT_FILE_NAME, binary=True)

  

main()

'''
model1.wv["men"]-model1.wv["good"]+model1.wv["women"]
similar_by_vector(vector, topn=10, restrict_vocab=None)'''
