# Harris McCullers 2019, all rights reserved


#imports
from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
warnings.filterwarnings(action = 'ignore') 
import gensim 
from gensim.models import Word2Vec 
import gensim.downloader as api
import numpy as np
from sklearn.manifold import TSNE
import re
import matplotlib.pyplot as plt
import pandas as pd

#UPDATE words here to create word cloud
WORDS = ["man", "woman", "boy", "girl", "mother", "father", "lady", "madame", "sir", "gentleman"]
MALE_WORDS = ["woman", "girl", "lady", "madame", "mother"]
FEMALE_WORDS = ["man", "boy", "sir", "gentleman", "father"]

def loadModel(fname):
    return gensim.models.KeyedVectors.load_word2vec_format(fname, binary=True)


def compareWord(model, startWord, wordList):
    '''compareWord takes a word and a list of words and
    finds the average similarty between the starter word
    and all the words in the list'''

    all = []

    count = 0
    for word in wordList:
        if word in model:
            count += 1
            all.append(model.similarity(startWord, word))

    return (sum(all)/len(all))


def compareLists(model, l1, l2):
    '''compareLists finds the average similarity
    between all items in l1 and l2'''
    l = []
    for word in l1:
        if word in model:
            l.append(compareWord(model, word, l2))

    return (sum(l)/len(l))


def parse(fname):
    '''parse takes in a filename and returns
    all of the words in a list format. It also
    makes them lowercase'''
    f = open(fname, "r", encoding="utf8")
    l = []
    for line in f:
        for word in line.split():
           l.append(word.lower())

    return l     


def thistothis(model, a, b, c):
    """ a:b::c::output"""
    #c - a + b
    vec = model.wv[c] - model.wv[a] + model.wv[b]
    return model.similar_by_vector(vec)[1:]

def main():
    model = loadModel(input("Enter filename of model: "))


    words =  WORDS
    wordDict = findsimilar(model, words, 10)


    N, L = wordsToVectorArray(model, wordDict)

    #groupA = red and groupB = blue
    testFunc(model, N, L, wordDict, FEMALE_WORDS, MALE_WORDS)
 

    return model

def findsimilar(model, wList, n):
    L = []
    D = {}

    
    for w in wList:
        D[w] = []
        for item in model.similar_by_word(word = w, topn = n):
            D[w].append(item[0])

    return D

def wordsToVectorArray(model, wordDict):
    '''This function takes in a wordDict (a dictionary) and converts it to a
    numpy array of vectors. '''
    wordList = []
    #turn dict to list
    for word in wordDict.keys():
        wordList += [word]
        wordList += wordDict[word]
    
    #remove duplicates
    wordList = list(dict.fromkeys(wordList))



    L = []
    A = []
    
    for w in wordList:
        L.append(model.wv[w])
        A.append(w)

    N = np.asarray(L)
    return N, A

def dictKeysToList(d, k):
    '''this helper function takes a dict d and a list
    of keys k and returns a list of all items in all
    key value pairs'''
    L = []
    for key in k:
        L += d[key]
    return L

def testFunc(model, li, vocab, highlightDict, groupA, groupB):
    #vocab = list(model.wv.vocab)
    #X = model[vocab]
    X = li
    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(X)
    df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(df['x'], df['y'], color='')
    
    for word, pos in df.iterrows():
        
        if word in highlightDict.keys():
            c = 'green'
        elif word in dictKeysToList(highlightDict, groupA) and word in dictKeysToList(highlightDict, groupB):
            c= "purple"
        elif word in dictKeysToList(highlightDict, groupA):
            c = "red"
        elif word in dictKeysToList(highlightDict, groupB):
            c = "blue"
        else:
            c = "black"


        ax.annotate(word, pos, color = c, fontname="Oswald")
        
    
    plt.show()
    


model = main()






