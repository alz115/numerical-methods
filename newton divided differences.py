'''
Нахождения значения функции в любой точке по ее известным значениям в нескольких других точках с помощью построения интерполяционного полинома Ньютона с использованием разделенных переменных.
'''

def get_divided_differences(x, y):
    n = len(y)
    coef = list(y)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def polynomial_newton(x_points, coef, x):
    n = len(coef) - 1
    result = coef[n]
    for i in range(n - 1, -1, -1):
        result = coef[i] + (x - x_points[i]) * result
    return result

print("Введите количество точек")
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

coeffs = get_divided_differences(x_points, y_points)
predict = polynomial_newton(x_points, coeffs, x)
print(predict)