# importing all necessary modules 
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
    model1 = loadModel(input("Enter filename of model: "))

    '''
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
    print(compareWord(model1, "diversity", parse("negativeWords.txt")))'''

    return model1

def findsimilar(model, wList, n):
    L = []
    A = []
    
    for w in wList:
        L.append(model.wv[w])
        A.append(w)
        for item in model.similar_by_word(word = w, topn = n):
            L.append(model.wv[item[0]])
            A.append(item[0])

    N = np.asarray(L)
    return N, A 

def testFunc(model, li, vocab, highlight = []):
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
        if word in highlight:
            ax.annotate(word, pos, color='green', fontname="Oswald")
        elif word in vocab[:50] and word in vocab[50:]:
            ax.annotate(word, pos, color='purple', fontname="Oswald")
        elif word in vocab[:50]:
            ax.annotate(word, pos, color='blue', fontname="Oswald")
        else:
            ax.annotate(word, pos, color='red', fontname="Oswald")
    
    plt.show()
    


model = main()




string = "We are looking for a Software Engineer who loves clean code, possesses a great attitude, and is not afraid to roll up their sleeves to get the job done. We are looking for someone with a great personality, ever-ready to learn, passionate about work and one that can fit into our company’s happy culture. Qualifications and certificates are secondary. Our ideal candidate should be strong in full-stack software development using Microsoft technologies."

#testFunc(model,  model[list(model.wv.vocab)], list(model.wv.vocab) )
N, L = findsimilar(model, ["male", "female"], 50)


testFunc(model, N, L, ["male", "female"])
 

