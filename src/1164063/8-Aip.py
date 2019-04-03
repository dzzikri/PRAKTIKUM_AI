# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 01:59:34 2019

@author: kiting13
"""

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(model.summary())