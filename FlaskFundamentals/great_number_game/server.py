from flask import Flask, redirect, request, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not session['somekey']:
        session['somekey'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def count():
    inputed = request.form('inputed')

    if int(inputed) is not int(session['somekey']):
        session['class'] = 'response'
        if int(inputed) > int(session['somekey']):
            session['response'] = 'TOO HIGH'
        else:
            session['response'] = 'TOO LOW'
    else:
        session['class'] = 'WIN'
        session['response'] = 'WIN'
        session['message'] = 'win ', str(session['somekey']), 'was the number!'

    return redirect('/')

app.run(debug=True)