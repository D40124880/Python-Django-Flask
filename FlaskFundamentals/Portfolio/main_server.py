from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_portfolio():
    return render_template('my_portfolio.html')

@app.route('/projects')
def my_projects():
    return render_template('my_projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)