
s = int(input("Число:"))
chislachet = []
chislanechet = []
chet = 0
nechet = 0

for q in range(s):
    if s%2 == 0:
        chislachet.append(s)
        s -= 1
        chet += 1
    else:
        chislanechet.append(s)
        s -= 1
        nechet += 1

print(f"""{chislachet} Чётных: {chet}""")
print(f"""{chislanechet} Нечётных: {nechet}""")