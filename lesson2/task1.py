# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

from data import fruits


def _max(iterable):
    max_value = 0
    for item in iterable:
        if item.__len__() > max_value:
            max_value = item.__len__()
    return max_value


def output_fruits():
    count = 0
    max_char_fruits = _max(fruits)
    for fruit in fruits:
        count += 1
        print(f"{count}. {fruit.rjust(max_char_fruits)}")


if __name__ == '__main__':
    output_fruits()
