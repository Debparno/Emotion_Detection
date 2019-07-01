# -*- coding: utf-8 -*-
"""
    Calculator
    ~~~~~~~~~~~~~~

    A simple Calculator made by Flask and jQuery.

    :copyright: (c) 2015 by Grey li.
    :license: MIT, see LICENSE for more details.
"""
import re
from flask import Flask, jsonify, render_template, request

from keras.models import load_model
# Run this cell to mount your Google Drive.
#from google.colab import drive
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences




app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    MAX_SEQUENCE_LENGTH = 30
    best_model =  load_model('checkpoint-1.111.h5')
    
    data_int_t = pad_sequences([[1, 72, 19, 38], [], [], [], []], padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = best_model.predict(data_test)
    
    a = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    b = request.args.get('number2', '0')
    m = re.match('-?\d+', a)
    n = re.match('-?\d+', b)
    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='I Catch a BUG!')
    if operator == '/':
        result = y_prob[0][0]
    else:
        result = y_prob[0][0]
    return jsonify(result = eval(str(y_prob[0][0]) + "+" + "0.0"))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
