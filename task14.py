w = input("Строка: ")
s = input("Символ: ")

index = -1
for i in range(len(w)):
    if w[i] == s:
        index = i
        break

if index != -1:
    print(f"Индекс: {index}")
else:
    print("Не найден")