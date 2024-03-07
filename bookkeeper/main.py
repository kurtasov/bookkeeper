from controller.crud_controller import CrudController


class App:
    def __init__(self):
        self.controller = CrudController()


if __name__ == "__main__":
    app = App()
    app.controller.create('Budget', {'monthly': 100_000,  # TODO: this should be a test
                                     'weekly': 25_000,
                                     'daily': 4_000})
