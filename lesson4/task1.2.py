# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_list1 = ['apple', 'banana', 'orange', 'kiwi']
fruits_list2 = ['banana', 'kiwi', 'grape', 'pineapple']

common_fruits = [fruit for fruit in fruits_list1 if fruit in fruits_list2]

print(common_fruits)
