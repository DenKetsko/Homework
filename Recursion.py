a = int(input("Введите сторону a прямоугольника: \n"))
b = int(input("Введите сторону b прямоугольника: \n"))

def Rec(width, length, n=0):
    if width == length:
        print("Сторона квадрата: ", length)
        return n + 1
    if width < length:
        print("Сторона квадрата: ", width)
        return Rec(width, length - width, n + 1)
    print("Сторона квадрата: ", length)
    return Rec(width - length, length, n + 1)

print(Rec(a, b))

"""char = input()
for i in range(a):
    if i == 0 or i == a - 1:
        for j in range(b):
            print(char, end='')
    else:
        print(char, end='')
        for j in range(1, b - 1):
            print(' ', end='')
        print(char, end='')
    print()"""