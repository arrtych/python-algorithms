# -*- coding: utf-8 -*-
choice = None
while choice != "0":
    print("0 - Выход\n1 - шифровать\n2 - дешифровать")
    choice= input("Ваш выбор: ")
    print()
    if choice == "0":
        print("До свидания")
    if choice == "1":
        print("Шифрование")
        alpha = ' abcdefghijklmnopqrstuvwxyz'
        print("Vvedite kluch: ")
        n = int(input())
        print("Vvedite frasu: ")
        s = input().strip()
        res = ''
        for c in s:
            res += alpha[(alpha.index(c) + n) % len(alpha)]
        print('Result: "' + res + '"')
    if choice == "2":
        print("Дешифрование")
        print("Vvedite kluch: ")
        n = int(input())
        print("Vvedite frasu: ")
        s = input().strip()
        res = ''
        for c in s:
            res += alpha[(alpha.index(c) - n) % len(alpha)]
        print('Result: "' + res + '"')






