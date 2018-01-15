def SortBubble(mylist):
    n = 1 
    while n < len(mylist):
         for i in range(len(mylist)-n):
              if mylist[i] > mylist[i+1]:
                   mylist[i],mylist[i+1] = mylist[i+1],mylist[i]
         n += 1
    return mylist
 
# profile.run('arr=SortBubble(s)')
list = [1,5,6,14,135,8,2]

print(SortBubble(list))