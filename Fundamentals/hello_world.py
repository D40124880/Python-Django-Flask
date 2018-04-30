print "Hello World!"

x = "Hello Python"
print x
y = 42
print y

#this is one way to make a comment

'''this is another way to make a comment'''

"""or"""

"""this is another"""

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'

print "this is a sample string"
name = "Zen"
print "My name is", name

name = "Zen"

print "My name is" + name

#whatever is inside the the format will replace the curly brackets
first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

#replacing %s %d %f with array information
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

#print upper case letters all
x = "Hello World"
print x.upper()
#output:
"HELLO WORLD"

#LISTS
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

drawer = ['documents', 'envelopes', 'pens']

print drawer[0] #prints documents
print drawer[1] #prints envelopes
print drawer[2] #prints pens

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];


my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3


my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]
