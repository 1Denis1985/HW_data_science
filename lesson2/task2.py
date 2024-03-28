# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
from random import randint

arr1 = [randint(1, 10) for _ in range(randint(10, 20))]
arr2 = [randint(1, 10) for _ in range(randint(10, 20))]


def delete_elements_from_list():
    set1 = set(arr1)
    set2 = set(arr2)
    print(f"Первый список: {arr1}")
    print(f"Второй список: {arr2}")
    print(f"Результат после удаления из  первого списка элементов, присутствующих во втором списке: ")
    print(list(set1 - set2))


if __name__ == '__main__':
    delete_elements_from_list()
