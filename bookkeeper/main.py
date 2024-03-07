from controller.crud_controller import CrudController
from view.main_window import MainWindow
from PySide6.QtWidgets import QApplication

class App(QApplication):
    def __init__(self):
        super().__init__()
        self.view = MainWindow()
        self.controller = CrudController()
        self.view.show()


if __name__ == "__main__":
    app = App()
    app.exec()
