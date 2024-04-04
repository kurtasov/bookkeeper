from controller.crud_controller import CrudController
from view.main_window import MainWindow
from PySide6.QtWidgets import QApplication


class App(QApplication):
    def __init__(self):
        super().__init__()
        self.view = MainWindow()
        self.controller = CrudController()
        self.view.set_controller(self.controller)

        self.view.refresh_categories()
        self.view.load_expenses_to_table()        
        self.view.show()


if __name__ == "__main__":
    app = App()
    app.exec()
