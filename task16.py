text = input("Введите строку: ")

result = ""

for char in text:
    if not char.isdigit(): 
        result += char

print("Результат:", result)