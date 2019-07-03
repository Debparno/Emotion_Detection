import re
from flask import Flask, jsonify, render_template, request

from keras.models import load_model
# Run this cell to mount your Google Drive.
#from google.colab import drive
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd
import pickle

app = Flask(__name__)
def init():
    global best_model
    # load the pre-trained Keras model
    best_model = load_model('models/gotCharactersDeathPredictions.h5')

@app.route('/process',methods= ['POST'])
def process():
    MAX_SEQUENCE_LENGTH = 30
    firstName = request.form['firstName']
    #lastName = request.form['lastName']
    #best_model =  load_model('BalanceNet1.h5')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    text = ["" for _ in range(5)]
    text[0] = str(firstName)
    sequences_test = tokenizer.texts_to_sequences(text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = best_model.predict(data_test)
    
    #output = firstName + lastName
    if (firstName):
        return jsonify({'output':'Neutral: ' + str(y_prob[0][0]) + ' ......Happiness: ' + str(y_prob[0][1]) +' ......Sadness: ' + str(y_prob[0][0]) + ' ......Hatred: ' + str(y_prob[0][0]) + ' ......Anger: ' + str(y_prob[0][0])})
    return jsonify({'error' : 'Missing data!'})

    
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

"""
@app.route('/', methods = ['POST'])
def index():
    MAX_SEQUENCE_LENGTH = 30
    
    best_model =  load_model('BalanceNet1.h5')
    #data2 = pd.read_csv('train.csv')
    text = request.form['firstName']
    x = text.split(' ')
    y = [int(k) for k in x]
    data_int_t = pad_sequences([y, [], [], [], []], padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = best_model.predict(data_test)
    #processed_text = text.upper()
    return jsonify({'request' : str(y_prob[0][0])})

"""
