#Что делает

#Создаёт список или преобразует объект в список.

#Пример

numbers = list(map(int, ["1", "2", "3"]))
print(numbers)

#Вывод:

#[1, 2, 3]

#Без list() это был бы map-объект.


fruits = list(["orange", "watermelon"])
print(fruits)

x = list("hello")
print(x)

#Задание

s = "25"
sn = list(map(str, [(s)]))
r = 25
rn = str(r)
c = 6
cn = str(c)
g = "4"
gn = int(g)

f = list("hello")
print(f)

a = list(map(str, ["3", "5", "1"]))
print(type(a))

e = list(map(str, ["654", "3", "abbb"]))
print(type(a))

b = list(map(int, ["7", "4", "3"]))
print(type(b))

print(f"""result:{a+b+e+f}""")
print("result2:",a+sn)
print("result3:",rn+cn)
print("result4:",r+gn)
