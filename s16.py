# -*- coding: utf-8 -*-
def deleteElement(stringA,stringB):
    count = 0
    newStr = ""
    for a in range(0,len(stringA)):
        if stringA[a] in list(stringB):
            count += 1
            stringA = stringA.replace(stringA[a], "-")
    stringA = stringA.replace("-","")
    print("Count: ", count)
    return stringA
v = deleteElement("abdbbbfhfhffdddddd0000beeee","abf000")
print(v)