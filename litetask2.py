w = int(input("Число белок:"))
s = int(input("Число орехов:"))

if w < 10000 and s < 10000 and w >= 0 and s >= 0:
    d = (s//w)
    e = (s-d*w)
else:
    d = "Нет"
    

print(f"""Досталось - {d}. Осталось - {e}.""")