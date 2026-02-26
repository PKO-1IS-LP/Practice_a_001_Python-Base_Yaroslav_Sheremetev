x1 = input("X: ")
y1 = input("Y: ")

x = float(x1)
y = float(y1)

def IsPointInSquare(x, y):
    return abs(x)<=1 and abs(y)<=1

def main():
    if IsPointInSquare(x, y):
        print("YES")
    else:
        print("NO")
    return 


main()
