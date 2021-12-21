import tensorflow as tf
from tensorflow import keras
import numpy as np
import scipy
from tensorflow.keras import layers
import ast
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.utils import class_weight

#0 = home win - 1 = away win
def samples_labels_generator(filename):
    games=[]
    fin = open(filename)
    for line in fin:
        line = ast.literal_eval(line)
        games.append(line)
    samples = []
    labels = []
    for game in games:
        sample = np.array([game[0][:], game[1][:]])
        samples.append(sample)
        labels.append(game[2][0])
    samples = np.array(samples)
    labels = np.array(labels)
    samples1, samples2 = samples[:, 0], samples[:, 1]

    return samples1, samples2, labels


data20082009 = samples_labels_generator("DataSet-09.txt")
data20092010 = samples_labels_generator("DataSet-10.txt")
data20102011 = samples_labels_generator("DataSet-11.txt")
data20112012 = samples_labels_generator("DataSet-12.txt")
data20122013 = samples_labels_generator("DataSet-14.txt")

input_data_1 = np.concatenate((data20082009[0], data20092010[0], data20102011[0],data20112012[0],data20122013[0]))
input_data_2 = np.concatenate((data20082009[1], data20092010[1], data20102011[1],data20112012[1],data20122013[1]))
labels = np.concatenate((data20082009[2], data20092010[2], data20102011[2],data20112012[2],data20122013[2]))
scaler = MinMaxScaler(feature_range=(0,1))
scalar = StandardScaler()
input_data_1 = tf.keras.utils.normalize(input_data_1)
input_data_2 = tf.keras.utils.normalize(input_data_2)
print(input_data_1)
#class_weights = class_weight.compute_class_weight('balanced',np.unique(labels),labels)

input1 = tf.keras.Input(shape = (4), name = 'input1')
input2 = tf.keras.Input(shape = (4), name = 'input2')
encoder = tf.keras.layers.Dense(4, activation='relu', kernel_initializer='zeros')
encoder2 = tf.keras.layers.Dense(4, activation='relu', kernel_initializer='zeros')
x1 = encoder(input1)
x2 = encoder(input2)
x1 = encoder2(input1)
x2 = encoder2(input2)
x = tf.keras.layers.concatenate([x1,x2])
x = tf.keras.layers.Dense(6, activation='relu',kernel_initializer='zeros')(x)
x = tf.keras.layers.Dense(4, activation='relu',kernel_initializer='zeros')(x)
x = tf.keras.layers.Dense(2, activation='relu',kernel_initializer='zeros')(x)
#x = tf.keras.layers.Dense(5, activation='relu')(x)
optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)
output = tf.keras.layers.Dense(1, activation='sigmoid', name = 'output')(x)
model = tf.keras.models.Model(inputs=[input1,input2], outputs=[output])
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'], shuffle = True)
ko = model.summary()
print(ko)
#model.fit([input_data_1,input_data_2],[labels], epochs = 100,)
#model.fit([data20102011[0],data20102011[1]],[data20102011[2]],epochs = 30, shuffle = False)
model.fit([data20112012[0],data20112012[1]],[data20112012[2]],epochs = 30, shuffle = False)
#model.fit([data20132014[0],data20132014[1]],[data20132014[2]],epochs = 30, shuffle = False)

#predictions = model.predict([data20092010[0], data20092010[1]])
#print(predictions)




'''
model = tf.keras.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(layers.Dense(64, activation='relu'))
# Add another:
model.add(layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss='mse',
              metrics=['accuracy'])
data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))
val_data = np.random.random((100, 32))
val_labels = np.random.random((100, 10))

model.fit(data, labels, epochs=10, batch_size=64, validation_data=(val_data, val_labels))
model.evaluate(data)
'''