from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojo():
    return render_template('dojos.html')

@app.route('/news')
def news():
    return render_template('news.html')

app.run(debug=True)