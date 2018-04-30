from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
   return redirect('/')
app.run(debug=True) # run our server

<html>
    <head>
       <title>Form Test Index</title>
    </head>
    <body>
      <h1>Index Page</h1>
      <h3>Create a User</h3>
      #<!-- read on to learn about form actions, we'll talk about the method in a later section -->
      <form action='/users' method='post'>
          Name: <input type='text' name='name'>
          Email: <input type='text' name='email'>
          <input type='submit' value='create user'>
      </form>
    </body>
</html>

----------------

Accessing Data
We can access form data with this syntax:

request.form['name_of_input']
----------------
We could then store that data:

my_data = request.form['name_of_input']
---------------------------------------------
Redirecting
Redirecting is critical, read the following carefully and implement it in the coming assignments.

Lastly, in our POST route we used the redirect method to send a new request to the '/' route. We can redirect to any route that we have defined:

return redirect('/route_goes_here')

#always redirect after handling any post
@app.route('/users', methods=['POST'])
def create_user():
   name = request.form['name']
   email = request.form['email']
	 # Here's the line that changed. We're rendering a template from a post route now
   return render_template('success.html')