# -*- coding: utf-8 -*-
s = input("Введите строку: ")
search = input("Введите искомый символ: ")
count = 0
id = 1;
while id != -1:
    id = s.find(search)
    if id >= 0:
        count += 1
    s = s[id+1:]
print ("символ(ы): " + search + " найден " + str(count) + " раз(а)")

