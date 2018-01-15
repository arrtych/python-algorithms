#! /usr/bin/env python
# Вводить числа через пробел как: 1 2 1 2 1 2 1
# a = [3,4,3,2,5,2]
a = [int(x) for x in input().split()]
print(a)
m = 0
for i in range(1, len(a)-1):
    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]):
        m += 1
print(m)