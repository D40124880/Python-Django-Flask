list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','sand']


import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

if compare(list_one, list_two):
    print "Both of these lists are the same"
else:
    print "Lists are different in either one or more areas"