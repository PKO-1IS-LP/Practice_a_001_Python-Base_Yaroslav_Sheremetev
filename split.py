#Что делает

#Разбивает строку на список по пробелу.

#Пример

s = "10 20 30"
print(s.split())

#Вывод:

#['10', '20', '30']

#Можно указать разделитель:

s = "10,20,30"
print(s.split(","))

#Задание
data = "apple,banana,cherry"
print(data.split(","))  # ['apple', 'banana', 'cherry']

ip = "192.168.1.1"
print(ip.split(".")) 


date = "2024-12-31"
print(date.split("-")) 