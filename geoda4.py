x1 = input("X: ")
y1 = input("Y: ")

x = float(x1)
y = float(y1)

def IsPointInArea(x, y):
    return x < y**2 and x > -y**2

def main():
    if IsPointInArea(x, y):
        print("YES")
    else:
        print("NO")

main()