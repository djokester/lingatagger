import pickle
from sklearn.metrics import confusion_matrix
import numpy as np
import tensorflowjs as tfjs

with open('X', 'rb') as fp:
    X_cnn = pickle.load(fp)
with open('Y', 'rb') as fp:
    Y_cnn = pickle.load(fp)
a = set(list(set("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
 
split1 = int(len(Y_cnn)*0.8)
X_train = X_cnn[:split1]
Y_train = Y_cnn[:split1]
X_test = X_cnn[split1:]
Y_test = Y_cnn[split1:]
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
valid_hindi = list(set(list("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
import numpy as np
def encodex(text):
    s = list(text)
    
    indices = []
    for i in s:
        indices.append(valid_hindi.index(i))
    encoded = np.zeros([18, len(valid_hindi)+1], dtype="int")
    #print(len(a)+1)
    k = 0
    for i in indices:
        encoded[k][i] = 1
        k = k + 1
    for i in range(18-len(list(s))):
        encoded[k+i][len(valid_hindi)] = 1
    return encoded

x = []
x.append(encodex('लड़का'))
x.append(encodex('लड़की'))
x.append(encodex('अर्चित'))
x.append(encodex('लड़का'))

x=np.array(x)
 
max_features = len(a)+1
 
 
for it in [['adam',64,0.6]]:
    opt = it[0]
    cnn_len = it[1]
    dropout = it[2]
    model = Sequential()             
    #model.add(Embedding(120, output_dim=18))

    model.add(Conv1D(cnn_len, 3, activation='relu', input_shape=(18, 120)))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(MaxPooling1D(3))
    model.add(GlobalAveragePooling1D())
    model.add(Dropout(dropout))
    model.add(Dense(1, activation='sigmoid'))
 

    model.compile(loss='binary_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    print("Training new model, loss:"+'binary_crossentropy'+", optimizer="+opt+", cnn_len="+str(cnn_len)+", dropoff="+str(dropout))
	
    model.fit(X_train, Y_train, batch_size=512, epochs=20,verbose =2)
    tfjs.converters.save_keras_model(model, 'jsmodel')
    print(model.predict(x))
    print(model.evaluate(X_test, Y_test))
    y_pred = model.predict(X_test, batch_size=512, verbose = 0)
    cm = confusion_matrix(Y_test, np.round(y_pred))
    recall = np.diag(cm) / np.sum(cm, axis = 1)
    precision = np.diag(cm) / np.sum(cm, axis = 0)
    print("recall: " + repr(recall))
    print("precision: " + repr(precision))
    a,b = np.unique(np.round(Y_test),return_counts=True)
    print("true count:" + repr(b))
    a,b = np.unique(np.round(y_pred),return_counts=True)
    print("predict count:" + repr(b))
    
    print("")
