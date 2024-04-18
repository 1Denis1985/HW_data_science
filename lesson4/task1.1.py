# Задание-1: Функция на python
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
def square_elements(input_list):
    return [x**2 for x in input_list]

input_list = [1, 2, 4, 0]
output_list = square_elements(input_list)
print(output_list)
