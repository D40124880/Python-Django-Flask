from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/ninja')
def ninja():
    img = "/static/imgs/tmnt.png"
    return render_template('ninja.html', img=img)

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        img = "/static/imgs/leonardo.jpg"
    elif color == "purple":
        img = "/static/imgs/donatello.jpg"
    elif color == "orange":
        img = "/static/imgs/michelangelo.jpg"
    elif color == "red":
        img = "/static/imgs/raphael.jpg"
    else:
        img = "/static/imgs/notapril.jpg"
    return render_template('ninja.html', img=img)

app.run(debug=True)


# blue = #25a9e3
# purple = #aa98c2
# orange = #fca05a
# red = #ee473

# to select images color on pixels: http://www.cs.uregina.ca/Links/class-info/325/PythonPictures/

# https://www.quora.com/How-do-I-swap-colors-in-an-image-using-OpenCV-and-Python
# https://stackoverflow.com/questions/38198379/how-do-i-change-pixel-values-for-an-image-in-python
# https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels


# or have extra color blocks to redirect to certain image