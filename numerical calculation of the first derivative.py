"""
Вычисление первой производной численными методами.
method: 'forward' - вперед, 'backward' - назад, 'central' - центральная
"""

def first_derivative(x, method,  h=1e-5 ):
    if method == 'forward':
        return (f(x + h) - f(x)) / h
    elif method == 'backward':
        return (f(x) - f(x - h)) / h
    elif method == 'central':
        return (f(x + h) - f(x - h)) / (2 * h)
    else:
        raise ValueError("Method must be 'forward', 'backward', or 'central'")


def f(x):
    return x**2
x = int(input())
method = input("Введите метод (forward/backward/central): ")

result = first_derivative( x, method=method)
print(f"Производная в точке x {result}")

