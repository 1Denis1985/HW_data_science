# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import itertools  # надо чаще использовать

# Определите имя файла
file_name = "random_number.txt"

# Сгенерируйте случайное 2500-значное число и запишите его в файл
random_number = ''.join(str(random.randint(0, 9)) for _ in range(2500))
with open(file_name, 'w') as file:
    file.write(random_number)

# Read the content of the file
with open(file_name, 'r') as file:
    content = file.read()

# Найдите самую длинную последовательность одинаковых цифр
max_sequence = max((len(list(group)), int(digit)) for digit, group in itertools.groupby(content))

print(
    f"Самая длинная повторяющаяся последовательность одинаковых цифр в файле'{file_name}' : {max_sequence[0]} встречается {max_sequence[1]} раз.")
