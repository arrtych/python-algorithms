import random
def addNumber(n):
    list = [random.randrange(-50, 50) for i in range(n)]
    # list = [5,50,-5,3,15]
    print("Generated list: ",list)
    for j in range(len(list) + 1):
        if list[j-1] < 0:
            x =list[j-1]
            list = list[:j] + [x*x] + list[j:]
    print("Result: ",list)

number = addNumber(5)
