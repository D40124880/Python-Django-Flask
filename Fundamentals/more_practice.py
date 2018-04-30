def say_hi(name):
    return 'Hi ' + name

greeting = say_hi('Martin')
print greeting

def add(a, b):
    x = a + b
    return x

sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 +sum2

# def multiply(arr,num):
#     print arr, num
#     for x in arr:
#         print x
#         x *= num
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

# def multiply(arr, num):
#     print arr, num
#     for x in arr:
#         print x
#         x *= num
#         print x
#     return arr
# a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b

# def multiply(arr,num):
#     print arr, num # output should be [2,4,10,16] 5
#     for x in arr:
#         print x
#         x *= num
#         print arr
#     return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b


# def multiply(arr, num):
#     for x in range(len(arr)):
#         arr[x] *= num
#     return arr
# a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b
# #output:
# >>>[10, 20, 50, 80]

# For in range to manipulate list elements
# NOT for in 
def multiply(arr,num):
    for x in range(len(arr)):
        print x
        arr[x] *= num
    print arr
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b


#MAKING LISTS OF TUPLES
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5, 6)
tuple_letters = "a", "b", "c", "d"
dog = ("Canis Familiaris", "dog", "carnivore", 12)

for data in dog[2]:
    print data

dog = dog + ("domestic",)
#output
#("canis familiarias", "dog", "carnivore", "man's best friend", "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#output
#("canis familiarias", "dog", "carnivore", "man's best friend", "domestic")

#GETTING THE RADIUS OF A CIRCLE
def get_circle_area(r):
    #return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


#importing libraries
import language
print language.translate(dog)


#DICTIONARIES
weekend = {"Sun": "Sunday", "Sat": "Saturday"}
capitals = {} #create empty dictionary
capitals ["svk"] = "Bratislava"
capitals ["deu"] = "Berlin"
capitals ["dnk"] = "Copenhagen"

print weekend["Sun"]
print capitals["dnk"]

#OR

#to print all keys
for data in capitals:
    print data
#another way to print all keys
for key in capitals.itervalues():
    print key
#to print the values
for val in capitals.itervalues():
    print val
#to print all keys and values
for key,data in capitals.iteritems():
    print key, " = ", data