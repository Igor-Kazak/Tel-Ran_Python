import datetime as dt

deposit = 10000
pincode = 0000


def cashmachine(pin, amount):
    now = dt.datetime.utcnow() + dt.timedelta(hours=2)
    time = now.strftime("%H:%M")
    result = f'${amount} в {time}'
    if pin == pincode:
        if amount <= deposit:
            printok(result)
        else:
            printminus(result)
    else:
        printerr(result)


def printok(result):
    print(f'Вы успешно сняли {result}. Остаток на счете: ${deposit - amount}.')


def printerr(result):
    print(f'Вы безуспешно пытались снять {result}. Неправильный ПИН.')


def printminus(result):
    print(f'Вы безуспешно пытались снять {result}. На счете недостаточно средств.')


pin = int(input("Здравствуйте!\nВведите ПИН:"))
amount = int(input("Введите сумму:"))

cashmachine(pin, amount)
