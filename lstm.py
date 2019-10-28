import pickle
 
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
from keras.layers import LSTM
 
max_features = len(a)+1
 
for loss_f in ['binary_crossentropy']:
    for opt in ['rmsprop','adam','nadam','sgd']:
        for lstm_len in [32,64,128,256]:
            for dropout in [0.4,0.45,0.5,0.55,0.6]:
                model = Sequential()
                model.add(LSTM(lstm_len))
                model.add(Dropout(dropout))
                model.add(Dense(1, activation='sigmoid'))
 
                model.compile(loss=loss_f,
                              optimizer=opt,
                              metrics=['accuracy'])
                print("Training new model, loss:"+loss_f+", optimizer="+opt+", lstm_len="+str(lstm_len)+", dropoff="+str(dropout))
                model.fit(X_train, Y_train, batch_size=512, validation_split = 0.2, epochs=20,verbose =2)
                score = model.evaluate(X_test, Y_test, batch_size=512, verbose = 0)
                print("")
                print("test score: " + str(score))
                print("")
                print("")
