import xml.dom.minidom
import requests

def kurs():
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    dom = xml.dom.minidom.parseString(r.text)
    dom.normalize()
    node1 = dom.getElementsByTagName("Value")[11]
    euro = float(node1.childNodes[0].nodeValue.replace(',', '.'))
    return euro


def rubtoeur(rub):
    if rub <= 0:
        print('Деньги из воздуха - возможно. Но не здесь.')
    else:
        result = round((rub / kurs()), 2)
        a = int(result)
        b = int((result - a) * 100)
        if (b % 10) == 1:
            print(f'По текущему курсу у Вас есть: {a} евро и {b} цент.')
        elif 2 <= (b % 10) <= 4:
            print(f'По текущему курсу у Вас есть: {a} евро и {b} цента.')
        else:
            print(f'По текущему курсу у Вас есть: {a} евро и {b} центов.')


try:
    rub = float(input("Введите сумму в рублях: "))
    rubtoeur(rub)
except ValueError:
    print("Вводить нужно только цифры")
