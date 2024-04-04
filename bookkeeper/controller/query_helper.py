from pony.orm import *
from bookkeeper.models.entities import *
import sqlite3


@db_session
def add_budget(monthly, weekly, daily):
    try:
        Budget(monthly=monthly, weekly=weekly, daily=daily)
    except Exception as e:
        print(e)  # TODO: This should be sent to GUI in a user-friendly manner

@db_session
def add_expense(amount, expense_date, category, comment):
    try:
        Expense(amount=amount, expense_date=expense_date, category=category, comment=comment)
    except Exception as e:
        print(e)  # TODO: This should be sent to GUI in a user-friendly manner


@db_session
def get_budget():
    try:
        q = select(b for b in Budget).order_by(lambda: desc(b.id)).limit(1)
        budget = q.to_list()[0]
        return tuple([budget.monthly, budget.weekly, budget.daily])  # TODO: return the object itself for GUI?
    except Exception as e:
        print(e)  # TODO: This should be sent to GUI in a user-friendly manner

@db_session
def get_category():
    try:
        q = select((c.parent.name, c.name) for c in Category if c.parent is not None)
        cats = list(q)
        return tuple(" > ".join(cat) for cat in cats)
    except Exception as e:
        print(e)


@db_session
def get_expense():
    try:
        q = select(b for b in Expense).order_by(lambda: desc(b.id))
        exspense = list(q)
        return exspense
    except Exception as e:
        print(e)

def load_data_from_db(self):
    db_connection = sqlite3.connect('db')  # Подставьте имя вашей базы данных
    cursor = db_connection.cursor()
    cursor.execute("SELECT amount, expense_date, category, comment FROM expenses")

    rows = cursor.fetchall()
    self.table.setRowCount(len(rows))


    db_connection.close()
