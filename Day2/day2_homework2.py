def total(tarif, hours, days):
    if tarif <= 0:
        print('Вы работаете бесплатно')
    else:
        if hours <= 0 or days <= 0:
            print('Вы не работали')
        elif hours > 24:
            print('На Земле в сутках всего 24 часа')
        else:
            if days > 31:
                print('На Земле в месяце не больше 31 дня')
            else:
                print('Ваша зарплата за месяц составила: ' + str(tarif *  hours * days) + ' того, в чём Вы её получаете')

try:
    tarif = int(input("Введите Вашу зарплату за 1 час: "))
    hours = int(input("Введите количество рабочих часов в день: "))
    days = int(input("Введите количество рабочих дней в месяце: "))
    total(tarif, hours, days)
except ValueError:
    print("Вводить нужно только цифры")