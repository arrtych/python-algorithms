#! /usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input("Введите число: "))
if n <=30000:
    l = [x for x in range(1, n + 1) if n % x == 0]  # все делители
    print(l)  # вывод всех делителей
    print("Количество натуральных делителей: " + str(len(l)))  # вывод количества делителей
else:
    print ("Число : " + str(n) + " > 30000")
