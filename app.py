
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def my_form_post():
    text = request.form['u']
    processed_text = text.upper()
    return processed_text

@app.route('/')
def my_form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


"""
import re
from flask import Flask, jsonify, render_template, request

from keras.models import load_model
# Run this cell to mount your Google Drive.
#from google.colab import drive
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd



app = Flask(__name__)


@app.route('/', methods = ['POST'])
def my_form_post():
    text = request.form['u']
    processed_text = text.upper()
    return processed_text

#x = 3
#y = 4
#best_model =  load_model('BalanceNet.h5') 
@app.route('/')
def index():
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run()
"""
