import csv
import os

# Загружаем данные о сотрудниках и отработанных часах
workers_data = []
with open('data/workers.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        workers_data.append({
            'name': row[0],
            'salary': float(row[1]),
            'norm_hours': float(row[2])
        })

hours_data = {}
with open('data/hours_of.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        hours_data[row[0]] = float(row[0])

# Рассчитываем зарплату каждого сотрудника
for worker, h_d in zip(workers_data, hours_data):
    name = worker['name']
    salary = worker['salary']
    norm_hours = worker['norm_hours']
    hours_worked = float(h_d)

    if hours_worked < norm_hours:
        # недоработка
        salary -= (norm_hours - hours_worked) * salary / norm_hours
    elif hours_worked > norm_hours:
        # переработка
        salary += (hours_worked - norm_hours) * salary * 2 / norm_hours

    # Выводим результаты
    print(f'{name}: {salary:.2f}')
