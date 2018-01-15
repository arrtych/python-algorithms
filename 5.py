# -*- coding: utf-8 -*-
s = "Эта книга адресована всем кто изучает Программирование."
# s = input("Введите строку: ")
s = s.split()
words =[]
checker = None
wordsCount = len(s)
true_words = wordsCount
for i in s:
    i = i.split()
    words.append(i)
print("words",s)
print("Всего слов:",wordsCount)
print("---")
for i in range(wordsCount):
    for c in words[i]:
        for cc in c:
            if 'а' <= cc <= 'я':
                checker = True
            else:
                true_words -=1
                break
        continue
print("Количество слов, содержащих только строчные русские буквы",true_words)
