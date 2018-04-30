#Multiples
# arr = []
# for x in range(1, 1001, 2):
#     print x

# for y in range(5, 1000001):
#     if(y % 5 == 0):
#         print y

a = [1, 2, 5, 10, 255, 3]
sum = 0
avg = 0
for w in range(0, len(a)):
    sum += a[w]
avg = sum / len(a)

print sum
print avg