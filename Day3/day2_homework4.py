import xml.dom.minidom
import requests


def currency(i):
    switcher = {
        'GPB': 2,
        'USD': 10,
        'EUR': 11
    }
    r = f'{switcher.get(i)}'
    return int(r)


def kurs():
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    dom = xml.dom.minidom.parseString(r.text)
    dom.normalize()
    node1 = dom.getElementsByTagName("Value")[currency(k)]
    curr = float(node1.childNodes[0].nodeValue.replace(',', '.'))
    return curr


def rubto(rub):
    if rub <= 0:
        print('Деньги из воздуха - возможно. Но не здесь.')
    else:
        result = round((rub / kurs()), 2)
        a = int(result)
        b = int((result - a) * 100)
        if (b % 10) == 1:
            print(f'По текущему курсу у Вас есть: {a} {k} и {b} цент.')
        elif 2 <= (b % 10) <= 4:
            print(f'По текущему курсу у Вас есть: {a} {k} и {b} цента.')
        else:
            print(f'По текущему курсу у Вас есть: {a} {k} и {b} центов.')


try:
    rub = float(input("Введите сумму в рублях: "))
    k = input("Введите валюту (GPB, USD, EUR): ")
    rubto(rub)
except ValueError:
    print("Ошибка ввода, будьте вниматальны")
