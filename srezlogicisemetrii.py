s = "level"

i = 0
print(s[i])                 # l
print(s[len(s) - 1 - i])    # l

i = 1
print(s[i])                 # e
print(s[len(s) - 1 - i])    # e

i = 2
print(s[i])                 # v
print(s[len(s) - 1 - i])    # v

#Задание

f = input("Слово: ").lower()
g = int(len(f))
e = list(f)
h = g
j = 0

for i in range(g):
    if e[h-g] == e[g-1]:
        print("Подходит буква")
        g -= 1
        j += 1
    else:
        print("Не полиндром")
    if j == h:
        print("Полиндром")


