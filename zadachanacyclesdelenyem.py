i = 20

#while i:
    #if i%7 == 0:
       # break
   # print(i)

for a in range(i):
    if i%7 == 0:
        break
    else:
        i -= 1
    print(i)

#Задание 1
s = 100
chisla = []
for q in range(s):
    if s%2 == 0:
        chisla.append(s)
        s -= 1
    else:
        s -= 1
print(chisla)

#Задание 2
e = 100
chisla2 = []
for w in range(e):
    if e%2 != 0:
        chisla2.append(e)
        e -= 1
    else:
        e -= 1
print(chisla2)
