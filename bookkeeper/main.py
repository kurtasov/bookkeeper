from controller.crud_controller import CrudController


class App:
    def __init__(self):
        self.controller = CrudController()


if __name__ == "__main__":
    app = App()
