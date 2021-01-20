def leapyear(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return 'Год високосный'
        else:
            return 'Год не високосный'
    else:
        return 'Год не високосный'


try:
    year = int(input("Введите год: "))
    print(leapyear(year))
except ValueError:
    print("Вводить нужно только цифры")