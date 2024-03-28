# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

from input_number import input_number


def check_age():
    age = input_number("Введите свой возраст: ")
    if age >= 18:
        if age > 100:
            print('Вы отлично сохранились')
        print("Доступ разрешен")
    elif age < 18:
        print("Извините, пользование данным ресурсом разрешено только с 18 лет")


if __name__ == "__main__":
    check_age()