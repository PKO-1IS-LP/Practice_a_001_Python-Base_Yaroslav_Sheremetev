# Сначала напишем функцию для нахождения минимума двух чисел
def min(a, b):
    """
    Функция возвращает меньшее из двух чисел
    """
    if a < b:
        return a
    else:
        return b



def min4(a, b, c, d):
    min_ab = min(a, b)
    min_cd = min(c, d)
    result = min(min_ab, min_cd)
    
    return result

# Считываем три целых числа
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Выводим результат работы функции min3
print(min4(a, b, c, d))