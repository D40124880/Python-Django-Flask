words = "It's thanksgiving day. It's my birthday, too!"
print words.replace('day', 'month', 1)

x = [2, 54, -2, 7, 12, 98]
print "The minimum is: " , min(x)

x = [2, 54, -2, 7, 12, 98]
print "The maximum is: ", max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
new_arr = []
new_arr.append(y[0])
new_arr.append(y[len(y)-1])
print new_arr

p = [19,2,54,-2,7,12,98,32,10,-3,6]
p.sort()
another_arr = []
number = (len(p)+1)/2
for w in range(0, number):
    another_arr.append(p[w])
p[0] = another_arr
print p