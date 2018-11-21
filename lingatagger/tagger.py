#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
import numpy as np
import lingatagger.genderlist as gndrlist
import lingatagger.tokenizer as tok
import gensim
import logging
import re
import sangita_data.hindi.sentences.loadsent as sents
import heapq

def genderdecode(genderTag):
    """
    one-hot decoding for the gender tag predicted by the classfier
    Dimension = 2.
    """
    genderTag = list(genderTag[0])
    index = genderTag.index(heapq.nlargest(1, genderTag)[0])
    if index == 0:
        return 'f'
    if index == 1:
        return 'm'
    if index == 2:
        return 'any'

def numericTagger(instr):
    """
    numericTagger is a regex based tagger that tags Numbers with the tag "num"
    :param instr: Can be a string, list of tokens or a list of tuples. 
    It can be the string to be tagged, tokenized string or even a pre-tagged string
    :type inst: string, list of strings, list of tuples
    
    :return: Returns a List of tuples of the form [(token1, genderTag), (token2, genderTag)...]
    :rtype: List of Tuples.
    """
    #lst = type([1, 2, 3])
    #tup = type(("Hello", "Hi"))
    #string = type("Hello")
    num_match = re.compile(r'([०१२३४५६७८९]+[\.\,]*)+[०१२३४५६७८९]+|([-+]*\d+[\.\,]*)+\d+|([०१२३४५६७८९]+|\d+)')
    if type(instr) == list:
        for index, item in enumerate(instr):
            if type(item) == tuple:
                if num_match.search(str(item[0])):
                    instr[index] = (instr[index][1], 'num')
            else:
                if num_match.search(str(item)):
                    instr[index] = (instr[index], 'num')
    else: 
        if type(instr) == str:
            instr = tok.tokenize(instr)
            numericTagger(instr)
        else:
            print("not supported")

    return instr

def defaultTagger(instr):
    """
    defaultTagger tags untagged tokens with "any"
    :param instr: Can be a string, list of tokens  
    It can be the string to be tagged, tokenized string 
    :type instr: string, list of strings, list of tuples
    
    :return: Returns a List of tuples of the form [(token1, genderTag), (token2, genderTag)...]
    :rtype: List of Tuples.
    """
    lst = type([1, 2, 3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    if type(instr) == lst:
        for index, item in enumerate(instr):
            if type(item) != tup:
                instr[index] = (instr[index], 'any')
    else: 
        if type(instr) == string:
            instr = tok.tokenize(instr)
            defaultTagger(instr)
        else:
            print("not supported")
    return instr

def lookupTagger(instr):
    """
    lookupTagger looks up the Dictionary formatches and tags the token if a match is found
    :param instr: Can be a string, list of tokens or a list of tuples
    It can be the string to be tagged, tokenized string or a pre-tragged list of tokens.
    :type instr: string, list of strings, list of tuples
    
    :return: Returns a List of tuples of the form [(token1, genderTag), (token2, genderTag)...]
    :rtype: List of Tuples.
    """
    lst = type([1, 2, 3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    gndrlst = gndrlist.drawlist()
    words = []
    genders = []
    for item in gndrlst:
        words.append(item.split("\t")[0])
        if(len(item.split("\t"))>2):
            genders.append("any")
        else:
            genders.append(item.split("\t")[1])
        
    tokens = set(words)
    
    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) == tup):
                if item[0] in tokens:
                    tag = genders[words.index(item[0])]
                    instr[index] = (instr[index][0],tag)
            else:
                if(type(item) != tup):
                    if item in tokens:
                        tag = genders[words.index(item)]
                        instr[index] = (instr[index], tag)
                
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            lookupTagger(instr)
            
        else:
            print("not supported")

    return(instr)

def encodex(text):
    s = list(text)
    a = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
    indices = []
    for i in s:
        indices.append(a.index(i))
    encoded = np.zeros([18, len(a)+1], dtype="int")
    k = 0
    for i in indices:
        encoded[k][i] = 1
        k = k + 1
    for i in range(18-len(list(s))):
        encoded[k+i][len(a)] = 1
    return encoded

def encodey(text):
    if text == "f":
        return [1,0,0]
    else:
        if text == "m":
            return [0,1,0]
        else:
            return [0,0,1] 

def genderclassify(sentence):
    """
    genderclassify tags with the help of multilayer perceptron classifier 
    trained over word vectors created with gensim's word2vec
    :param sentence: string to be tokenized and tagged
    :type sentence: string
    
    :return: Returns a List of tuples of the form [(token1, genderTag), (token2, genderTag)...]
    :rtype: List of Tuples.
    """
    sentence = tok.wordtokenize(sentence)   
    genders = gndrlist.drawlist()
    lst = []
    a = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
    for i in genders:
        x = i.split("\t")
        if type(numericTagger(x[0])[0]) != tuple:
            lst.append(x)    
    
    x = []
    y = []
    for i in lst:
        a = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
        count = 0
        for ch in list(i[0]):
            if ch not in a:
                count+=1
        if count == 0:
            x.append(encodex(i[0]))
            y.append(encodey(i[1]))

    X = np.array(x)
    Y = np.array(y)
    model = Sequential()
    model.add(Conv1D(64, 3, activation='relu', input_shape=(18, 130)))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(3))
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.fit(X, Y, batch_size=16, epochs=10)

    result = []
    for token in sentence:
        a = model.predict(np.array(encodex(token).reshape((1,18,130))))
        result.append((token, genderdecode(a)))
    
    return(result)
    
          
def Tagger(instr):
    """
    Combines the result of all four taggers for accuracte tagging
    :param sentence: string to be tokenized and tagged
    :type sentence: string
    
    :return: Returns a List of tuples of the form [(token1, genderTag), (token2, genderTag)...]
    :rtype: List of Tuples.
    """
    instr = genderclassify(instr)
    instr = lookupTagger(instr)
    instr = numericTagger(instr)
    instr = defaultTagger(instr)
    
    return(instr)

if __name__ == '__main__':
    input_str = 'नीरजः हाँ माता जी! स्कूल ख़त्म होते सीधा घर आऊँगा'
    lst = ["1", "2", "3", "4"]
    string = "०१२३४५६७८९ ०१२३"
    """
    print(numericTagger(lst))
    print(numericTagger(string))
    """
    print(Tagger(input_str))
    print(genderclassify(input_str))
    print(lookupTagger(input_str))
