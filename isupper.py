#Что делает

#Проверяет, заглавная ли буква.

print("A".isupper())  # True
print("a".isupper())  # False


#Задание

a = input()
an = list(map(str, [a]))
print(an)
al = len(a)
d = 0
def ff():
    for i in range (len(al)):
        print(d+1)


print(f"""{(str(an).isupper())}""")