from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello world!"

@app.route('/')
def hello_world1():
    print "Hello Other world from server"
    return render_template('index.html')

app.run(debug=True)

# from flask import Flask  # Import Flask to allow us to create our app.
# app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
#                          # directly, or importing it as a module.
# @app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
#                          # function to the '/' route. This means that whenever we send a request to
#                          # localhost:5000/ we will run the following "hello_world" function.
# def hello_world():
#   return 'Hello World!'  # Return the string 'Hello World!' as a response.
# app.run(debug=True)      # Run the app in debug mode.


#-----route structure
@app.route('/some_route')
def some_function_name():
    //your code