from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Программа для ведения бюджета")
        self.setFixedSize(300, 350)

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('1'))
        self.layout.addWidget(QLabel('2'))
        self.layout.addWidget(QLabel('3'))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
