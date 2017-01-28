import numpy as np
from keras.models import Sequential
from keras.layers import Dense


model = Sequential()
model.add(Dense(12, input_dim=1, init='uniform', activation='relu'))    #input layer: 12 neurons, expects 1 input
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(3, init='uniform', activation='sigmoid'))               #output layer: 3 outputs