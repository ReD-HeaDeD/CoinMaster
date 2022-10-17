from model import Coins


def save_db(): #запись данных
    for row in open('coin_list.txt').readlines():
        f = Coins.create(data=row.strip().split(':')[0],
                         name=row.strip().split(':')[1],
                         dollar=row.strip().split(':')[2])
        f.save()


save_db()

