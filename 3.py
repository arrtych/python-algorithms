# -*- coding: utf-8 -*-
# Вводить двоичные числа через как: 0.5
even = 0
odd =0
evenMultiply = 1
oddSum = 0
choice = None
lst=[]
N=int(input('Количество элементов: '))
print("---")
for i in range(N):
    choice=float(input('Введите число: '))
    if choice == 55555:
        N = i -1
        break
    else:
        lst.append(choice)
print(lst)
if all([ v == 0 for v in lst ]) :
    evenMultiply = 0
for k, v in enumerate(lst):
    if (k + 1) % 2 == 0:
        even += 1
        evenMultiply *= v
    else:
        odd += 1
        oddSum += v
print("сумма чисел с нечётными номерами: ", oddSum, ",количество слагаемых", odd)
print("произведение чисел с чётными номерами", evenMultiply, ",количество сомножителей", even)



