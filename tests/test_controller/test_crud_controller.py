import pytest
from bookkeeper.controller.crud_controller import CrudController


@pytest.fixture
def crudctrl():
    return CrudController()


def test_add_and_read_budget(crudctrl):
    crudctrl.create('Budget', {'monthly': 100_000,
                                     'weekly': 25_000,
                                     'daily': 4_000})
    budget_tup = crudctrl.read('Budget')
    assert budget_tup == (100000.0, 25000.0, 4000.0)
