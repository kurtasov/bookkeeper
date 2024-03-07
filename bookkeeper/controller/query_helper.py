from pony.orm import *
from bookkeeper.models.entities import Budget


@db_session
def add_budget(monthly, weekly, daily):
    try:
        Budget(monthly=monthly, weekly=weekly, daily=daily)
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