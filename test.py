from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from keras.layers import Dense, Conv2D, Flatten
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import lingatagger.genderlist as gndrlist
import lingatagger.tokenizer as tok
from lingatagger.tagger import *
import re
import heapq

def encodex(text):
    s = list(text)
    a = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
    indices = []
    for i in s:
        indices.append(a.index(i))
    encoded = np.zeros([18, len(a)+1], dtype="int")
    #print(len(a)+1)
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

genders = gndrlist.drawlist()
lst = []
a = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
for i in genders:
	x = i.split("\t")
	if type(numericTagger(x[0])[0]) != tuple:
		lst.append(x)    

x = []
y = []
for i in lst:
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
model.add(Conv1D(80, 8, activation='relu', padding='same', input_shape=(18, 120)))
model.add(Conv1D(64, 6, activation='relu', padding='same'))
#model.add(Conv1D(32, 2, activation='relu', padding='same'))
#model.add(Conv1D(16, 2, activation='relu', padding='same'))
#model.add(MaxPooling1D(4))
model.add(GlobalAveragePooling1D())
#model.add(Flatten())
#model.add(Dropout(0.5))
#model.add(Dense(15, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(3, activation='softmax'))

model.summary()
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
model.fit(X, Y, batch_size=16, epochs=10, validation_split=0.2)
sentence = tok.wordtokenize('मजा अर्चि अर्चिता')

result = []
for token in sentence:
	a = model.predict(np.array(encodex(token).reshape((1,18,120))))
	print((token, genderdecode(a)))

