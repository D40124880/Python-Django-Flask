from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return "Hello World"
    return render_template('index.html', name="Jay")

app.run(debug=True)


<body>
    <h1>Hello World</h1>
    <p>My name is {{ name }} </p>
</body>

{{ this is for some variable }}
{% this is for some expression %}
---------------------------------------
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase='Hello', times=5)

app.run(debug=True)


<html>
    <head>
      <title>My First Template</title>
    </head>
    <body>
      <h3>My flask template with embedded Python-like code</h3>
      #<!-- this will output the value of our phrase variable -->

      <p>Phrase: {{ phrase }}</p>
      #<!-- this will output the value of our times variable -->

      <p>Times: {{ times }}</p>
      #<!-- here is an example of embedding a for-loop in our code -->
      
      {% for x in range(0,times): %}
      <p>{{ phrase }}</p>
      {% endfor %}
      #<!-- here is an example of embedding an if statement in our code -->

      {% if phrase == "hello" %}
 <p>The phrase says hello</p>
      {% endif %}
    </body>
</html>
----------------------------------------------------------------------------------------------------------------
#ALL IN HTML ------ create folder static for css && javascript
CSS
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style_sheet.css') }}">

javascript
<script type='text/javascript> src="{{ url_for('static', filename='my_script.js')}}"></script>

if its inside a folder to call it from
<script type='text/javascript> src="{{ url_for('static', filename='js/my_script.js')}}"></script>


#<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style_sheet.css') }}">
#<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
#<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">


#<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style_sheet.css') }}">
#<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
#<!-- linking an image -->
<img src="{{ url_for('static', filename='img/my_img.png') }}">
