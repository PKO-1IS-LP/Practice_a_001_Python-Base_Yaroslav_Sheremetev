s = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))

positive = 0
negative = 0
zero = 0

for num in numbers[:s]:  
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f"Положительных: {positive}")
print(f"Отрицательных: {negative}")
print(f"Нулей: {zero}")