from flask import Flask 
from flask import render_template 
from flask import request
import random 

FLAG_SECOND_HALF = 'X3RoNHRfcjNzdGZ1bF80UElzX2RvbnRfdzBya19seWtfZDFzfQ=='
PORT=5000

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/secret', methods = ['GET','POST'])
def secret():
    if (request.method == 'GET'):
        return render_template('secret.html') 
    elif (request.method == 'POST'):
        return FLAG_SECOND_HALF

if __name__ == '__main__': 
    app.run(debug=False, port=PORT, host="0.0.0.0")