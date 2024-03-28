def input_number(description: str = 'Введите число: ') -> int:
    count_input = 0
    count_attempt = 10
    while count_input < 10:
        count_input += 1
        try:
            number_str: str = input(description)
            number: int = int(number_str)
            if str(number_str)[0] == "0":
                raise ValueError
            return number
        except ValueError:
            print(f"Введите число, вы ввели {number_str}. У вас осталось: {count_attempt - count_input} попыток.")
            continue
