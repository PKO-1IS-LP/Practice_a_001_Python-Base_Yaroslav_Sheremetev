#Что делает

#Применяет функцию к каждому элементу.

#Пример

numbers = map(int, ["1", "2", "3"])
print(numbers)

#Процесс:

#int("1") → 1
#int("2") → 2
#int("3") → 3

#Результат:

#[1, 2, 3]

#Задание

float_numbers = [1.5, 2.7, 3.9, 4.2, 5.0]
a = str(float_numbers.split(","))
print(a)