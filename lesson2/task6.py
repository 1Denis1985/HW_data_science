import math


def find_floor_room(N):
    # Находим номер этажа
    # На каждом этаже количество комнат увеличивается на единицу. Последовательность этого увеличения представляет собой арифметическую прогрессию.
    floor = math.ceil((math.sqrt(8 * N + 1) - 1) / 2)

    # Находим порядковый номер комнаты слева на этаже
    left_room = N - (floor - 1) * floor // 2

    return floor, left_room


if __name__ == '__main__':
    # Пример использования:
    N = int(input("Введите номер комнаты"))  # Номер комнаты
    floor, left_room = find_floor_room(N)
    print(floor, left_room)
