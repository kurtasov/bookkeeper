from pony.orm import *
from bookkeeper.models.entities import *
import sqlite3

@db_session
def get_expense():
    try:
        q = select(b for b in Expense).order_by(lambda: desc(b.id)).limit(1)
        exspense = list(q)
        return tuple([exspense.expense_date, exspense.amou])
    except Exception as e:
        print(e)


print (get_expense())