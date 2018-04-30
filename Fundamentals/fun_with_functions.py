def odd_even():
    for x in range(0, 2001):
        if(x % 2 != 0):
            print "Number is", x, ". This is an odd number."
        elif(x % 2 == 0):
            print "Number is", x, ". This is an even number."
odd_even()

def multiply(arr, num):
    for y in range(0, len(arr)):
        arr[y] *= num
    return arr
a = [2, 4, 10, 16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    new_array = []
    temp = ['1',]
    for w in range(0, len(arr)):
        new_array.append(arr[w] * temp)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x

#[10, 20, 50, 80]
# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,]]