# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
from random import randint

arr = [randint(1, 100) for _ in range(randint(10, 100))]


def new_arr():
    _new_arr = []
    for item in arr:
        if item % 2 == 0:
            _new_arr.append( item / 4)
        else:
            _new_arr.append(item * 2)
    return _new_arr


if __name__ == '__main__':
    print(new_arr())
