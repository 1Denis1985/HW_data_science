# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    str_ticket = str(ticket_number)
    parity = True if not (_len := len(str_ticket)) % 2 else False
    if parity:
        res = (sum(map(int, str_ticket[:_len // 2])) == sum(map(int, str_ticket[_len // 2:])))
    else:
        res = (sum(map(int, str_ticket[:_len // 2 + 1])) == sum(map(int, str_ticket[_len // 2:])))

    return "Это счастливый билет" if res else "Ссори, это не счастливый билет"


if __name__ == "__main__":
    print(lucky_ticket(123006))
    print(lucky_ticket(12321))
    print(lucky_ticket(436751))