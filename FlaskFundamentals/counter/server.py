from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['posts'])
def counting():
    if not 'counter' in session:
        session['counter'] = 0
    else:
        session['counter'] += 2
    return render_template('index.html', counter=session['counter'])

@app.route('/2')
def reset():
    if 'counter' > 0:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

app.run(debug=True)