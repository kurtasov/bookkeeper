from models import entities


class App:
    def __init__(self):
        try:
            entities.db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
            entities.db.generate_mapping(create_tables=True)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = App()
