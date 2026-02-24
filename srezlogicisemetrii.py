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

f = input("slovo: ")
a = f[::-1]

if a == f:
    print("Полиндром")
else:
    print("Не полиндром")