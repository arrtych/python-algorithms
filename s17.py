list =[0,2,2,3,5,-33,1,0,2,-2,3,-5]
def min(list):
    low = list[0] # need to start with some value
    for i in range(0,len(list)):
        if list[i] < low:
            low = list[i]
    return (str("Index: ") + str(i)+ str(" Value: ") +str(low))
print (min(list))