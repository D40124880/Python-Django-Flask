import random

def grading():
    for i in range(0,10):
        num = random.randint(60,101)
        if(num >= 90 and num <=100):
            print "Score:", num, "Your grade is A"
        elif(num >= 80 and num <=89):
            print "Score:", num, "Your grade is B"
        elif(num >= 70 and num <=79):
            print "Score:", num, "Your grade is C"
        elif(num >= 60 and num <=69):
            print "Score:", num, "Your grade is D"


grading()
        

