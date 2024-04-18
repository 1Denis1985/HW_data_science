# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.


def parse_fraction(fraction_str):
    parts = fraction_str.split(' ')
    whole_part = 0
    numerator = 0
    denominator = 1

    if len(parts) == 1:  # Если только целое
        fraction_part = parts[0]
    elif len(parts) == 2:  # если часть и целое
        whole_part = int(parts[0])
        fraction_part = parts[1]
    else:
        raise ValueError("Неверный формат дроби")

    if '/' in fraction_part:
        numerator, denominator = map(int, fraction_part.split('/'))
    else:
        numerator = int(fraction_part)

    return whole_part, numerator, denominator


def to_mixed_fraction(whole_part, numerator, denominator):
    if whole_part == 0:
        return f"{numerator}/{denominator}"
    elif numerator == 0:
        return str(whole_part)
    else:
        return f"{whole_part} {numerator}/{denominator}"


def add_fractions(fraction1, fraction2):
    whole_part1, numerator1, denominator1 = parse_fraction(fraction1)
    whole_part2, numerator2, denominator2 = parse_fraction(fraction2)

    numerator_sum = whole_part1 * denominator1 * denominator2 + numerator1 * denominator2 + whole_part2 * denominator1 * denominator2 + numerator2 * denominator1
    denominator_sum = denominator1 * denominator2

    return to_mixed_fraction(numerator_sum // denominator_sum, numerator_sum % denominator_sum, denominator_sum)


def subtract_fractions(fraction1, fraction2):
    whole_part1, numerator1, denominator1 = parse_fraction(fraction1)
    whole_part2, numerator2, denominator2 = parse_fraction(fraction2)

    numerator_diff = whole_part1 * denominator1 * denominator2 + numerator1 * denominator2 - (
            whole_part2 * denominator1 * denominator2 + numerator2 * denominator1)
    denominator_diff = denominator1 * denominator2

    return to_mixed_fraction(numerator_diff // denominator_diff, abs(numerator_diff) % denominator_diff,
                             denominator_diff)


def sum_diff_fractions():
    fraction1 = input("Введите первую дробь в формате 'n x/y': ")
    fraction2 = input("Введите вторую дробь в формате 'n x/y': ")

    print("Результат сложения:", add_fractions(fraction1, fraction2))
    print("Результат вычитания:", subtract_fractions(fraction1, fraction2))


# Пример использования:
if __name__ == "__main__":
    sum_diff_fractions()
