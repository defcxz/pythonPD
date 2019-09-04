from random import *

a = []

for i in range(10):
    a.append(randint(1,100))
    print (a[i]),

print ("")
print (a)
max = max(a)
min = min(a)
largo = len(a)
sum = sum(a)
del (a[5])



