from datetime import date
from pony.orm import *

db = Database()

class Expense(db.Entity):
    id = PrimaryKey(int, auto=True)
    Amount = Required(float)
    Date = Required(date, default=lambda: date.today())
    category = Required('Category')
    Comment = Optional(str)


class Budget(db.Entity):
    id = PrimaryKey(int, auto=True)
    Daily = Required(float, default=1000)
    Monthly = Required(float, default=31000)
    Annual = Required(float)
    Weekly = Required(str, default=1000)



class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    Name = Required(str)
    expenses = Set(Expense)
    Parent = Optional('Category', reverse='Parent')


