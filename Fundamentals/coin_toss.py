import random

def coin_toss():
    tails = 0
    heads = 0
    for x in range(0, 5000):
        num = random.randint(0, 101)
        if (num % 2 != 0):
            print "Attempt#", x, "Throwing a coin... It's a head! ... Got", heads, "heads(s) so far and", tails, "tails(s) so far"
            heads += 1
        elif (num % 2 == 0):
            print "Attempt#", x, "Throwing a coin... It's a tail! ... Got", heads, "heads(s) so far and", tails, "tails(s) so far"
            tails += 1
coin_toss()