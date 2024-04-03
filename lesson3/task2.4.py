# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def define_parallelogram(a1: tuple | list, a2: tuple | list, a3: tuple | list, a4: tuple | list):
    if a1[0] == a2[0] and a2[1] == a3[1] and a3[0] == a4[0] and a4[1] == a1[1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(define_parallelogram((1, 2), (1, 3), (5, 3), (5, 2)))
    print(define_parallelogram((1, 3), (1, 3), (5, 3), (5, 2)))