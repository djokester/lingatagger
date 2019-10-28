import pickle
from sklearn.metrics import confusion_matrix
import numpy as np

with open('X', 'rb') as fp:
    X_lstm = pickle.load(fp)
with open('Y', 'rb') as fp:
    Y_lstm = pickle.load(fp)
a = set(list(set("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
 
split1 = int(len(X_lstm)*0.8)
X_train = X_lstm[:split1]
Y_train = Y_lstm[:split1]
X_test = X_lstm[split1:]
Y_test = Y_lstm[split1:]
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM, Bidirectional
 
max_features = len(a)+1
 
 
for it in [['nadam',256,0.6],['nadam',256,0.55],['nadam',128,0.4],['nadam',128,0.45],['adam',256,0.55]]:
    opt = it[0]
    lstm_len = it[1]
    dropout = it[2]
    model = Sequential()
    model.add(Bidirectional(LSTM(lstm_len)))
    model.add(Dropout(dropout))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    print("Training new model, loss:"+'binary_crossentropy'+", optimizer="+opt+", lstm_len="+str(lstm_len)+", dropoff="+str(dropout))
    model.fit(X_train, Y_train, batch_size=512,epochs=20,verbose =2)
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
