x1 = input("X: ")
y1 = input("Y: ")

x = float(x1)
y = float(y1)

def IsPointInCircle(x, y):
    return (x + 1)**2 + (y - 1)**2 <= 4

def IsPointInArea(x, y):
    return 

def main():
    if IsPointInCircle(x, y) and IsPointInArea(x, y):
        print("YES")
    else:
        print("NO")

main()