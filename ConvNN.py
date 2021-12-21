#import tensorflow as tf
import numpy as np
import re
import pandas as pd

files_train = ["ConvDataSet-09.txt"]
files_train += [f"ConvDataSet-{val}.txt" for val in range(10,13)]
files_train += [f"ConvDataSet-{val}.txt" for val in range(14,17)]
files_test = [f"ConvDataSet-{val}.txt" for val in range(17,20)]

def read_data(files):

    x_data = []
    y_data = []

    for file in files:
        with open(file) as f:
            lines = f.readlines()
            x1_data = [0]*len(lines)
            x2_data = [0]*len(lines)
            y_data =  [0]*len(lines)
            i = 0

            for line in lines:
                line = re.sub('[\[\]]', '', line).strip().strip(" ")
                line =",".join(line.split(", "))
                splitted = line.split(";")
                x1 = [float(val) for val in splitted[0].split(",")]
                x2 = [float(val) for val in splitted[1].split(",")]
                y  = [int(splitted[2][0].split(","))]
                x_data.append([x1,x2])
                y_data.append(y)

    return np.array(x_data),np.array(y_data)






x_train,y_train = read_data(files_train)
x_test,y_test = read_data(files_test)

#x_train = tf.keras.utils.normalize(x_train,axis=1)
#x_test = tf.keras.utils.normalize(x_test,axis=1)

train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))


