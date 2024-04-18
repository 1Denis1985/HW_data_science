# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


queens_positions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]


def is_attacking(queen1, queen2):
    return queen1[0] == queen2[0] or queen1[1] == queen2[1] or abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1])


def check_queens_attack(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            if is_attacking(queens_positions[i], queens_positions[j]):
                return "YES"
    return "NO"


result = check_queens_attack(queens_positions)
print(result)
