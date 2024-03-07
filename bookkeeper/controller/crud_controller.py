from bookkeeper.models.entities import db
import bookkeeper.controller.query_helper as qh


class CrudController:
    def __init__(self):
        try:
            db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)  # TODO: Move DB file name to config / dotenv
            db.generate_mapping(create_tables=True)
        except Exception as e:
            print(e)

    def create(self, entity, params):
        if entity == 'Budget':
            qh.add_budget(monthly=params['monthly'], weekly=params['weekly'],
                          daily=params['daily'])
            return

        raise NotImplementedError(f'Добавление для сущности {entity} не реализовано!')

    def read(self, entity):
        raise NotImplementedError(f'Чтение для сущности {entity} не реализовано!')

    def update(self, entity):
        raise NotImplementedError(f'Изменение для сущности {entity} не реализовано!')

    def delete(self, entity):
        raise NotImplementedError(f'Удаление для сущности {entity} не реализовано!')