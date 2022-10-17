from peewee import *

db = SqliteDatabase('coin.db') #drivers


class Coins(Model):
    data = CharField()
    name = CharField()
    dollar = CharField()

    class Meta:
        database = db


Coins.create_table()
