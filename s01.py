#! /usr/bin/env python
n = int(input("Enter a value n: "))
hours = n//60%24
minutes = n%60
if n < 60:
    if n <= 9:
        extra = "0"
    else:
        extra = ""
    result = "00:" + extra + str(minutes)
elif n > 60:
    if minutes <= 9:
        extraM = "0"
    else:
        extraM = ""
    if hours <= 9:
        extraH = "0"
    else:
        extraH = ""
    result = extraH + str(hours) + ":" + extraM + str(minutes)
print (result)