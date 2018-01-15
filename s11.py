print('m')
m = input()  # исходное сообщение
m = ' '.join(m.split())
k = "АБВГ"  # ключ

k *= len(m) // len(k) + 1  # подгоняем ключ
c = ''.join([chr((ord(j) + ord(k[i]) + 32) % 32 + ord('А')) for i, j in enumerate(m)])  # шифруем
print(c) # LXFOPVEFRNHR
print('c')
c = input()  # шифрованое сообщение
c = ' '.join(c.split())
k = "АБВГ"  # ключ

k *= len(c) // len(k) + 1  # подгоняем ключ
m = ''.join([chr((ord(j) - ord(k[i]) + 32) % 32 + ord('А')) for i, j in enumerate(c)])  # расшифровываем
print(m) # ATTACKATDAWN
