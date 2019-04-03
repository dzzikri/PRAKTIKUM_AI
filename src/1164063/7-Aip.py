# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 01:59:47 2019

@author: kiting13
"""

model = Sequential([
    Dense(100, input_dim=np.shape(train_input)[1]),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
    ])