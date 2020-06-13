import pickle
import numpy as np
with open('X', 'rb') as fp:
    X_cnn = pickle.load(fp)
with open('Y', 'rb') as fp:
    Y_cnn = pickle.load(fp)
valid_hindi = (list(set("ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ-")))
 
split1 = int(len(Y_cnn)*0.8)
X_train = X_cnn
Y_train = Y_cnn
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D, Bidirectional, LSTM
 
max_features = len(valid_hindi)+1

test = ["अभिनेता","लेखक","यात्री","भाई","व्यवसायी","रसोइया","बेटी","अभियंता","पिता","दादा","दादी","वकील","माता","आरक्षक","चिकित्सक","प्रधानमंत्री","विक्रेता","बहन","सिपाही","बेटा","दरजी","अध्यापक","लेखक","चिड़िया","भौंरा","तितली","बिल्ली","चूज़ा","गाय","हिरन","कुत्ता","गधा","बत्तख","हाथी","मछली","घोड़ा","शेर","बन्दर","मोर","सुअर","खरगोश","झींगा","दगाबाज़","हंस","बाघ","कछुआ","सेब","केला","तुलसी","मिर्च","नारियल","अंगूर","चमेली","दाल","गंधना","आम","पुदीना","सिन्दूर","प्याज़","आलू","कद्दू","मूली","गुलाब","चंदन","सूर्यमुखी","अजवायन","टमाटर","तरबूज","एशिया","कतार","ब्रिटेन","भवन","शहर","महाद्वीप","देश","घर","गंगा","दुकान","भारत","पुस्तकालय","पर्वत","सगर","पाकिस्तान","उद्यान","भोजनालय","नदी","विद्यालय","दुकान","देवालय","अमरीका","चिड़ियाघर","पलंग","डिब्बा","रोटी","मक्खन","कुरसी","द्वार","डोसा","घर","तेल","पतलून","अङ्कनी","चावल","नमक","समोसा","साड़ी","कमीज","मसाला","शक्कर","मिठाई","मेज़","चाय","पानी","खिड़की","वास्तुकला","कला","बैडमिंटन","जीव-विज्ञान","शतरंज","क्रिकेट","नाच","खेल","इतिहास","भूगोल","पत्रकारिता","साहित्य","गणित","म्यूज़िक","जीवाश्मिकी","कविता","विज्ञान","पहेली","दौड","अध्ययन","तैराकी","टेनिस","दूरी","योग","सुन्दरता","रंग","आत्मविश्वास","ईर्ष्या","समय","हास्य","भूख","करुणा","ज्योति","प्यार","मनस","एकता","गौरव","ऋतु","आकाश","आवाज","चाल","तीव्रता","भोर","सूर्यास्त","समय","मौसम","विद्या"]
print(len(test))
testy = ["masculine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","masculine","masculine","feminine","masculine","feminine","masculine","masculine","masculine","masculine","feminine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","feminine","feminine","masculine","feminine","masculine","masculine","masculine","feminine","masculine","feminine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","feminine","feminine","masculine","masculine","feminine","feminine","feminine","masculine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","masculine","masculine","masculine","masculine","masculine","feminine","feminine","masculine","masculine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","feminine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","feminine","masculine","masculine","masculine","masculine","feminine","feminine","masculine","masculine","masculine","feminine","feminine","masculine","feminine","feminine","feminine","feminine","masculine","feminine","feminine","feminine","masculine","masculine","masculine","masculine","masculine","feminine","masculine","masculine","feminine","masculine","masculine","masculine","feminine","feminine","masculine","feminine","feminine","masculine","feminine","masculine","feminine","masculine","feminine","masculine","masculine","feminine","masculine","masculine","feminine","feminine","feminine","feminine","masculine","feminine","masculine","feminine","masculine","feminine","feminine","feminine","feminine","masculine","masculine","masculine","feminine"]
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
fc= 0
mc = 0
def encodey(text):
    if text == "f":
        return [1]#,0,0]
    elif text == "m":
        return [0]#,0,1]

    else:
        return [0,1,0] 
l1 = []
for a,b in zip(test,testy):
    if len(a) > 18:
        continue
    l1.append((a, b[0]))

l1 = list(set(l1))

xt = []
yt = []
for a,b in l1:
    if(b[0]=='m'):
        mc+=1
    else:
        fc+=1
    if mc >=55 and b[0] == 'm':
        continue
    xt.append(encodex(a))
    yt.append(encodey(b[0]))

    
print(fc ,mc) 
#xt = np.array(xt)
#yt = np.array(yt)
Xu = (X_cnn).tolist()
Yu = (Y_cnn).tolist()
for t,yt3 in zip(xt, yt):
    if t.tolist() in Xu:

        print(Xu.index(t.tolist()))
        print(yt3, Y[Xu.index(t)])
    else:
        print("NEW")
print(X_train.shape)
print(xt.shape)
for loss_f in ['binary_crossentropy']:
    for opt in ['nadam','adam','nadam','sgd']:
        for lstm_len in [256,64,128]:
            for dropout in [0.6,0.45,0.5,0.55,0.6]:
                model = Sequential()             
                #model.add(Embedding(120, output_dim=18))

                model = Sequential()
                model.add(Bidirectional(LSTM(lstm_len)))
                model.add(Dropout(dropout))
                model.add(Dense(1, activation='sigmoid'))


                model.compile(loss='binary_crossentropy',
                              optimizer=opt,
                              metrics=['accuracy'])
                print("Training new model, loss:"+'binary_crossentropy'+", optimizer="+opt+", lstm_len="+str(lstm_len)+", dropoff="+str(dropout))
                model.fit(X_train, Y_train, validation_data = (xt,yt), batch_size=512,epochs=10,verbose =2)
                score = model.evaluate(xt, yt, batch_size=512, verbose = 0)
                print("")
                print("test score: " + str(score))
                print("")
                print("")
                yt2 = model.predict(xt, batch_size=512,verbose=0)
                m = 0
                f = 0
                a = 0
                for i,y2 in zip(range(0,len(yt2)),yt2):
                    y= y2
                    print(test[i])
                    if y < 0.5:
                        print("f " + testy[i][0])
                        f+=1
                    else:
                        print("m " + testy[i][0])
                        a+=1
                print(m,f,a)
