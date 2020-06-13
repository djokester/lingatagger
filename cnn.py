import pickle
 
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
 
max_features = len(a)+1
 
for loss_f in ['binary_crossentropy']:
    for opt in ['rmsprop','adam','nadam','sgd']:
        for cnn_len in [32,64,128]:
            for dropout in [0.4,0.45,0.5,0.55,0.6]:
                model = Sequential()
                model.add(Conv1D(cnn_len, 3, activation='relu', input_shape=(18, 120)))
                model.add(Conv1D(64, 3, activation='relu'))
                model.add(MaxPooling1D(3))
                model.add(GlobalAveragePooling1D())
                model.add(Dropout(dropout))
                model.add(Dense(1, activation='sigmoid'))
 
                model.compile(loss=loss_f,
                              optimizer=opt,
                              metrics=['accuracy'])
                print("Training new model, loss:"+loss_f+", optimizer="+opt+", cnn_len="+str(cnn_len)+", dropoff="+str(dropout))
                model.fit(X_train, Y_train, batch_size=512, validation_split = 0.2, epochs=20, verbose=2)
                score = model.evaluate(X_test, Y_test, batch_size=512, verbose = 0)
                print("")
                print("test score: " + str(score))
                print("")
                print("")
