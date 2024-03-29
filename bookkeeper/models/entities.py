"""Модуль создает классы таблиц баз данных.
Создан с помощью PonyORM"""

from datetime import date
from pony.orm import *


db = Database()


class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    expenses = Set('Expense')
    parent = Optional('Category', reverse='parent')


class Expense(db.Entity):
    id = PrimaryKey(int, auto=True)
    amount = Required(float)
    expense_date = Required(date, default=date.today())
    added_date = Required(date, default=date.today())
    comment = Optional(str)
    category = Required(Category)


class Budget(db.Entity):
    id = PrimaryKey(int, auto=True)
    monthly = Required(float, default=56000)
    weekly = Required(float, default=14000)
    daily = Required(float, default=2000)
