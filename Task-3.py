import random
n = int(input("Введите размер списка: \n"))
A = []
for i in range(n):
    a = random.randint(0,99)
    A.append(a)
s = sum(A)
l = len(A)
a = s/l

print(A)
print("Сумма элементов: ", s)
print("Среднее арифметическое: ", a)