EURO = 89.95


def rubtoeur(rub):
    if rub <= 0:
        print('Деньги из воздуха - возможно. Но не здесь.')
    else:
        result = round((rub / EURO), 2)
        a = int(result)
        b = int((result - a) * 100)
        print(f'По текущему курсу у Вас есть: {a} евро и {b} центов.')


try:
    rub = float(input("Введите сумму в рублях: "))
    rubtoeur(rub)
except ValueError:
    print("Вводить нужно только цифры")