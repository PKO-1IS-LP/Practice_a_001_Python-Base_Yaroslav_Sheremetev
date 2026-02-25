s = int(input("Число:"))
chisla = []

for q in range(s):
    if s%3 == 0 and s%5 == 0:
        chisla.append(s)
        s -= 1
    else:
        s -= 1
sum = sum(chisla, start=0)

print(sum)