# Python program to generate word vectors using Word2Vec 
  
# importing all necessary modules 
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
  
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec 
  

def main():
    #  Reads ‘alice.txt’ file 
    sample = open("googleMemo.txt", "r", encoding="utf8") 
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

    # Rome is to Italy as China is to what?
    #then the equation Rome -Italy + China would return Beijing. No kidding.


    # Create CBOW model 
    model1 = gensim.models.Word2Vec(data, min_count = 1,  
                                size = 100, window = 5) 

    #model1.save("123.model")
    #gensim.models.KeyedVectors.load_word2vec_format("123.model")


    
    # Create Skip Gram model 
    model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100, 
                                                window = 5, sg = 1) 
    #model2.similarity('war', 'good'))

    print("Positive Words:")

    print("Women: ")
    print(compareWord(model1, "women", parse("positiveWords.txt")))
    print("Men:")
    print(compareWord(model1, "men", parse("positiveWords.txt")))
    print("Diversity:")
    print(compareWord(model1, "diversity", parse("positiveWords.txt")))


    print("Negative Words")

    print("Women: ")
    print(compareWord(model1, "women", parse("negativeWords.txt")))
    print("Men:")
    print(compareWord(model1, "men", parse("negativeWords.txt")))
    print("Diversity:")
    print(compareWord(model1, "diversity", parse("negativeWords.txt")))




def compareWord(model, startWord, wordList):

    all = []

    count = 0
    for word in wordList:
        if word in model:
            count += 1
            all.append(model.similarity(startWord, word))

    return (sum(all)/len(all))


def compareLists(model, l1, l2):
    l = []
    for word in l1:
        if word in model:
            l.append(compareWord(model, word, l2))

    return (sum(l)/len(l))


def parse(fname):
    f = open(fname, "r", encoding="utf8")
    l = []
    for line in f:
        for word in line.split():
           l.append(word.lower())

    return l     


main()

'''
model1.wv["men"]-model1.wv["good"]+model1.wv["women"]
similar_by_vector(vector, topn=10, restrict_vocab=None)'''