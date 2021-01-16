import datetime as dt


def toprint(name, birth):
    now = dt.datetime.utcnow()
    year = int(now.strftime("%Y"))
    age = year - birth
    lastdigit = age % 10
    result = ''

    if age > 0:
        if 5 <= lastdigit <= 9 or lastdigit == 0:
            result = f'{name}, Вам {year - birth} лет'
        elif lastdigit == 1:
            result = f'{name}, Вам {year - birth} год'
        elif 2 <= lastdigit <= 4:
            result = f'{name}, Вам {year - birth} года'
    else:
        result = 'Что-то не так с Вашей датой рождения'
    print(result)


name = input("Здравствуйте!\nВведите Ваше имя: ")

try:
    birth = int(input("Введите год рождения: "))
    toprint(name, birth)
except ValueError:
    print("Был введен некорректный год рождения")
