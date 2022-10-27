import sqlite3 as lite
import numpy as np
import sys


con = lite.connect('coin.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT dollar FROM coins WHERE data LIKE '%11 September 2022%'")
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

    spisok_copy = spisok_1.copy()
    spisok_2 = spisok_copy
    #print(len(spisok_2))
    for spisok_2_elem in range(len(spisok_2)):
        if len(spisok_2[spisok_2_elem]) != spisok_2[0]:
            spisok_2[spisok_2_elem] = spisok_2[0]
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
            print("{:.15f}".format(my_rho[my_rho_index]))
            my_rho_index += 1


    print(my_rho)