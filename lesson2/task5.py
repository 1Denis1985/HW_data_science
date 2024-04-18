# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# # Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '-2.10.3001'
# date = '01.22.1001'
# date = '1.12.1001'

def check_date(date):
    if len(date) != 10:
        return False

    day, month, year = date.split('.')

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False

    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False

    if day < 1 or day > 31:
        return False

    if month < 1 or month > 12:
        return False

    if year < 1 or year > 9999:
        return False

    return True


if __name__ == '__main__':
    # Примеры использования
    date1 = '01.11.1985'
    date2 = '01.22.1001'
    date3 = '1.12.1001'
    date4 = '-2.10.3001'

    print(check_date(date1))  # True
    print(check_date(date2))  # False
    print(check_date(date3))  # False
    print(check_date(date4))  # False
