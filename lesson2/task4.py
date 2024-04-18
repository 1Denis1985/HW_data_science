# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.


# вычислите и выведите y

def calculate_y(equation, x):
    k, b = list(map(float, [x for x in equation if x.isdigit()]))
    y = k * x + b
    return y


# Пример использования

if __name__ == '__main__':
    equation = '2x + 3'
    x = 2
    y = calculate_y(equation, x)
    print(y)
