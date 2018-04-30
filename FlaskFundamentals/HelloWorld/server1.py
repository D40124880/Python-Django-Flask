from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_to_all():
    return render_template('index1.html')

app.run(debug=True)