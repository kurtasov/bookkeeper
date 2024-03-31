from pony.orm import *
from bookkeeper.models.entities import *
@db_session
def get_expense():
    expenses = Expense._select_all() # Получение всех расходов из базы данных


print (get_expense())