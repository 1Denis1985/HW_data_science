# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
from pprint import pprint
from input_number import input_number


def output_digits_number() -> None:
    number = input_number()
    count_output = 0
    pprint(f"Числа слева направо:")
    for char in str(number):
        count_output += 1
        pprint(f"Число {count_output}: {char}")


if __name__ == "__main__":
    output_digits_number()
