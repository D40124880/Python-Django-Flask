# listing = [1, 5, 2, 7, 4]
# listing = ['magical','unicorns']
listing = ['magical unicorns',19,'hello',98.98,'world']
sum_all = 0
count_num = 0
count_str = 0
string = ''

for x in range(0, len(listing)):
    if isinstance(listing[x], int) or isinstance(listing[x], float):
        sum_all += listing[x]
    elif isinstance(listing[x], str):
        string += listing[x] + ' '
    else:
        continue

if sum_all != 0:
    count_num = 1
if string != '':
    count_str = 1

if count_num == 1 and count_str == 1:
    print "The list you entered is of mixed type"
    print "String: ", string
    print "Sum: ", sum_all
elif count_num == 1:  
    print "The list you entered is of integer type"
    print sum_all
elif count_str == 1:
    print "The list you entered is of string type"
    print "String: " + string
else:
    print "Nope!"