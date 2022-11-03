import sqlite3 as lite
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
    SQL_veriable += f"data LIKE '%{select_data}%' "
    if amount_data > index_amount_data + 1:
        SQL_veriable = SQL_veriable + 'or '
    print(SQL_veriable)
    index_amount_data += 1
"""в этой части кода мы обращаемся к БД и создаем цикл на создание списка коинов из БД за те даты, которые брали выше и переводим в FLOAT, обросив лишние символы"""
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
    #print(spisok_1)
    print('Введите номер из списка, по которому хотите произвести корреляцию: ')
    """в этой части кода мы создаем второй список копии первого списка с 1 коином, для реализации корреляции"""
    spisok_copy = spisok_1.copy()
    spisok_2 = spisok_copy
    #print(len(spisok_2))
    number_spisok_2 = int(input())
    for spisok_2_elem in range(len(spisok_2)):
        if len(spisok_2[spisok_2_elem]) != spisok_2[number_spisok_2]:
            spisok_2[spisok_2_elem] = spisok_2[number_spisok_2]
    spisok_1 = [float(spisok_1_float) for spisok_1_float in spisok_1]
    spisok_2 = [float(spisok_2_float) for spisok_2_float in spisok_2]
    print(spisok_1)
    print(spisok_2)
    x_simple = np.array(spisok_1)
    y_simple = np.array(spisok_2)
    my_rho = np.divide(x_simple, y_simple)

    my_rho_index = 0
    for my_rho_elem in range(len(my_rho)):
        if my_rho[my_rho_elem] != 1.0:
            print("{:f}".format(my_rho[my_rho_index]))
            my_rho_index += 1


    print(my_rho)