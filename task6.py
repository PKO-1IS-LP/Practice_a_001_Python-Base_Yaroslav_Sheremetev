s = int(input("Введите число: "))

two = 0
three = 0
twothree = 0

for q in range(s):
    if s%2 == 0:
        if s%3 == 0:
            s -= 1
            twothree += 1
        else:
            two += 1
            s -= 1
    if s%3 == 0:
        if s%2 == 0:
            s -= 1
            twothree += 1
        else:
            three += 1
            s -= 1    
    else:
        s -= 1

print(f"""На 2 - {two}. На 3 - {three}. На два и три - {twothree}.""")