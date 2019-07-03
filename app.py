import re
from flask import Flask, jsonify, render_template, request

from keras.models import load_model
# Run this cell to mount your Google Drive.
#from google.colab import drive
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pandas as pd

app = Flask(__name__)

"""
@app.route('/', methods = ['POST'])
def my_form_post():
    MAX_SEQUENCE_LENGTH = 30
    
    best_model =  load_model('BalanceNet.h5')
    #data2 = pd.read_csv('train.csv')
    text = request.form['u']
    x = text.split(' ')
    y = [int(k) for k in x]
    data_int_t = pad_sequences([y, [], [], [], []], padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = best_model.predict(data_test)
    #processed_text = text.upper()
    return jsonify({'request' : str(y_prob[0][0])})
 """

@app.route('/process',methods= ['POST'])
def process():
    MAX_SEQUENCE_LENGTH = 30
    best_model =  load_model('BalanceNet.h5')
    """
    firstName = request.form['firstName']
    #lastName = request.form['lastName']
    text = str(firstName)
    #b = str(lastName)
    x = text.split(' ')
    y = [int(k) for k in x]
    data_int_t = pad_sequences([y, [], [], [], []], padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = best_model.predict(data_test)
    """
    if (firstName):
        return jsonify({'output':'Full Name: ' + 'debu'})
    return jsonify({'error' : 'Missing data!'})

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

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
