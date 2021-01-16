PRICE = 5.5


def total(consump, s):
    if consump <= 0:
        print('Вечный двигатель невозможен. Пока.')
    else:
        if s <= 0:
            print('Вам не надо никуда ехать')

        else:
            print('Расходы на поездку составят: ' + str(float((s / 100.0) * PRICE * consump)) + ' шекелей')


try:
    consump = int(input("Введите расход бензина (л) на 100км: "))
    s = int(input("Введите расстояние (км): "))
    total(consump, s)
except ValueError:
    print("Вводить нужно только цифры")