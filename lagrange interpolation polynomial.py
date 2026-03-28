'''
Нахождения значения функции в любой точке по ее известным значениям в нескольких других точках с помощью построения интерполяционного полинома Лагранжа.
'''

def lagrange(x_points, y_points, x):
    n = len(x_points)
    result = 0

    for i in range(n):
        L_i = 1
        for j in range(n):
            if j != i:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * L_i
    return result

print("Напишите количество точек")
n = int(input())

x_points = []
y_points = []

print("Введите координаты точек (x y):")
for i in range(n):
    print(f"Точка {i + 1}:")
    x, y = map(float, input().split())
    x_points.append(x)
    y_points.append(y)

x = float(input("Введите x для вычисления: "))

result = lagrange(x_points, y_points, x)
print('Ответ: ', result)