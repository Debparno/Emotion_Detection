# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYJ7dIG1mloLgLTFvVF6uyvz_PFfMRZF
"""

from keras.models import load_model

# Run this cell to mount your Google Drive.
from google.colab import drive
drive.mount('/content/drive')

best_model =  load_model('drive/My Drive/text-emotion-classification-master/checkpoint-1.111.h5')

MAX_SEQUENCE_LENGTH = 30



from keras.preprocessing.text import Tokenizer

from keras.preprocessing.sequence import pad_sequences

#import pickle


data_int_t = pad_sequences([[1, 72, 19, 38], [], [], [], []], padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
y_prob = best_model.predict(data_test)

#print(" Neutral: ",y_prob[0][0], " Happy: ",y_prob[0][1], " Sad: ",y_prob[0][2], " Hate: ",y_prob[0][0], " Anger: ",y_prob[0][0])

#y_prob[0][0] + y_prob[0][1] + y_prob[0][2] + y_prob[0][3] + y_prob[0][4]
