# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 02:09:28 2019

@author: kiting13
"""


loss, acc = model.evaluate(test_input, test_labels, batch_size=32)
#%%
print("Done!")
print("Loss: %.4f, accuracy: %.4f" % (loss, acc))
