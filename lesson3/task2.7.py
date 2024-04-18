fruits_file = "data/fruits.txt"

# Считываем список фруктов из файла
with open(fruits_file, 'r', encoding="utf-8") as file:
    fruits = [fruit.strip() for fruit in file.readlines()]

# Создаем словарь, где ключ - первая буква слова, значение - список слов
fruits_dict = {}
for fruit in fruits:
    first_letter = fruit[0].upper()
    if first_letter in fruits_dict:
        fruits_dict[first_letter].append(fruit)
    else:
        fruits_dict[first_letter] = [fruit]

# Получаем список букв русского алфавита
russian_alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

# Записываем фрукты в файлы
for letter in russian_alphabet:
    letter = letter.upper()
    if letter in fruits_dict:
        with open(f"data/fruits_{letter}.txt", 'w', encoding="utf-8") as file:
            file.write('\n'.join(fruits_dict[letter]))