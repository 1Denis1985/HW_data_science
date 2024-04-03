# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# функция на четность
def odd(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


# новый фильтр
def filter(in_num, arr):
    return [in_num(item) for item in arr]


if __name__ == "__main__":
    print(filter(odd, [2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
