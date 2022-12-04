import sqlite3 as lite
import math

import numpy
import numpy as np
import sys


con = lite.connect('coin.db')
"""в этой части кода мы создаем условие на создание иттераций по количеству запросов обращения к БД"""
print('количество дат, которое хотите выбрать: ')
amount_data = int(input()) #сколько дат из БД нужно вытянуть
SQL_veriable = ''
index_amount_data = 0
while index_amount_data < amount_data:
    print('введите дату: ')
    select_data = str(input())
    print('введите монетку: ')
    select_coin = str(input())
    SQL_veriable += f"data LIKE '%{select_data}%' AND name LIKE '{select_coin}'"
    if amount_data > index_amount_data + 1:
        SQL_veriable = SQL_veriable + 'or '
    #print(SQL_veriable)
    index_amount_data += 1
"""в этой части кода мы обращаемся к БД и создаем цикл на создание списка коинов из БД за те даты, 
которые брали выше и переводим в FLOAT, обросив лишние символы"""
with con:
    cur = con.cursor()
    cur.execute(f"SELECT dollar FROM coins WHERE {SQL_veriable}")
    rows = cur.fetchall()
    text = ''
    index = 0
    add_float = 0.0
    spisok_1 = []
    for row in rows:
        text = rows[index][0]
        text = text.replace('$', '')
        text = text.replace(',', '')
        spisok_1.append(text)
        index += 1
    """в этой части кода мы рассчитываем меру риска Шарпа"""
    spisok_1 = [float(spisok_1_float) for spisok_1_float in spisok_1]
    print(spisok_1)

    Rp = float(spisok_1[-1] - spisok_1[0])
    print(f'Доходность портфеля равна: {Rp}')

    Rf = float(4.6872)
    print(f'Доходность безрискового актива равна: {Rf}')
    """ниже рассчитываем среднюю цену коина за год"""
    all_coin_in_year = 0
    index_spisok = 0
    for element_spisok_1 in spisok_1:
        if index_spisok <= len(spisok_1):
            all_coin_in_year += spisok_1[index_spisok]
            index_spisok += 1
    average_value = all_coin_in_year / len(spisok_1)
    """а этим кодом уже рассчитываем среднеквадратичное значение коина"""
    value = 0
    index_spisok_1 = 0
    for element_spisok_2 in spisok_1:
        if index_spisok <= len(spisok_1):
            value += (spisok_1[index_spisok_1] - average_value) ** 2
            index_spisok_1 += 1
    Qr = value / len(spisok_1) #и этой формулой уже риск портфеля
    print(f'риск портфеля равен: {Qr}')

    S = (Rp - Rf) / Qr #формула шарпа
    print(S)
    sqrt = S ** (0.5)
    print(f'мера риска Шарпа равна: {"{:f}".format(sqrt.real)}')

    std = np.std(spisok_1)
    print(std)
