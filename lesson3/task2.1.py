# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    # рекурсия нахождения числа фибоначчи
    def fi(n):
        if n in (1, 2):
            return 1
        return fi(n - 1) + fi(n - 2)

    # список формирующийся от n до m через рекурсию
    res = []
    for i in range(n, m):
        res.append(fi(i))

    return res


if __name__ == "__main__":
    print(fibonacci(5, 15))