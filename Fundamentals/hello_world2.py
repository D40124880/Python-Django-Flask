if statement:
if <condition>:
    #do something
#if-else statement:
elif <condition>:
    #do something
else:
    #do something

age = 15
if age >= 18:
    print 'Legal age'
else:
    print 'You are so young!'

if age >= 18:
    print 'Legal Age'
elif age == 17:
    print 'You are amazing!'
else:
    print 'You are so young!'



for count in range(0, 5):
    print "looping-", count



for <counter> in <sequence or range>:
    #do something

my_list = [4, 'dog', 99, ['lst', 'inside', 'anmother'], 'hello world']
for element in my_list:
    print element

for count in range(0, 5):
    print "looping - ", count

count = 0
while count < 5: #notice the colon!
    print 'looping - ', count
    count += 1

while <expression>


for val in "string":
    if val == "i":
        break
    print val

s
t
r


for val in "string":
    if val == "i":
        continue
    print val
s
t 
r 
n 
g 


#the pass statement is used when a statement is required syntactically but you do not want any command or code to exxecute
class EmptyClass:
    pass

for val in my_string:
    pass

x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print "Final else statement"
3
2
1
Final else statement

&&

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "Final else statement"

3
2
1

