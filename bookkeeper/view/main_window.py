""" Модуль главного окна пользовательского интерфейса программы"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton,
                               QLineEdit, QComboBox, QTableWidget, QAbstractItemView)
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QDialog, QInputDialog)
from bookkeeper.new_transaction import Ui_Dialog



from PySide6.QtWidgets import QHeaderView



from pony.orm import *
# Подключение к существующей базе данных

from bookkeeper.models.entities import db

from bookkeeper.models.entities import Category

from bookkeeper.models.entities import Expense

from bookkeeper.models.entities import Budget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()



        self.controller = None
        self.setWindowTitle("Программа для ведения бюджета")
        self.setFixedSize(500, 500)

        self.layout = QVBoxLayout()

        self.budget_monthly = QLabel('Бюджет на месяц: ')
        self.budget_weekly = QLabel('Бюджет на неделю: ')
        self.budget_daily = QLabel('Бюджет на день: ')
        self.layout.addWidget(self.budget_monthly)
        self.edit_budget_monthly = QLineEdit()
        self.layout.addWidget(self.edit_budget_monthly)
        self.layout.addWidget(self.budget_weekly)
        self.edit_budget_weekly = QLineEdit()
        self.layout.addWidget(self.edit_budget_weekly)
        self.layout.addWidget(self.budget_daily)
        self.edit_budget_daily = QLineEdit()
        self.layout.addWidget(self.edit_budget_daily)

        expenses_table = QTableWidget(4, 20)

        expenses_table.setColumnCount(4)
        expenses_table.setRowCount(20)
        expenses_table.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split())

        header = expenses_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        expenses_table.setEditTriggers(
            QAbstractItemView.DoubleClicked) # возможности настройки редактирования ячеек - https://doc.qt.io/qt-6/qabstractitemview.html#EditTrigger-enum
        expenses_table.verticalHeader().hide()

        self.layout.addWidget(expenses_table)

        self.budget_button = QPushButton('Задать бюджет')
        self.layout.addWidget(self.budget_button)
        self.budget_button.clicked.connect(self.on_budget_button_click)




        # Определение обработчика события
        def on_add_transaction_button_click(self):
            # Здесь можно добавить логику для открытия диалогового окна или других действий, связанных с добавлением транзакции
            pass

        self.create_category_button = QPushButton('Создать категорию')
        self.layout.addWidget(self.create_category_button)
        self.create_category_button.clicked.connect(self.on_create_category_button_click)


        self.delete_category_button = QPushButton('Удалить категорию')
        self.layout.addWidget(self.delete_category_button)
        self.delete_category_button.clicked.connect(self.on_delete_category_button_click)


        self.add_transaction_button = QPushButton('Добавить транзакцию') # Создание кнопки "Добавить транзакцию"
        self.layout.addWidget(self.add_transaction_button) # Добавление кнопки на экран
        self.add_transaction_button.clicked.connect(self.on_add_transaction_button_click)  # Привязка обработчика события к кнопке



        self.category = QComboBox(self)
        self.layout.addWidget(QLabel('Выберите категорию расхода:'))
        self.layout.addWidget(self.category)




        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def set_controller(self, controller):
        self.controller = controller

    def refresh_budgets(self):
        bdgt = self.controller.read('Budget')
        self.budget_monthly.setText('Бюджет на месяц: ' + str(bdgt[0]))
        self.budget_weekly.setText('Бюджет на неделю: ' + str(bdgt[1]))
        self.budget_daily.setText('Бюджет на день: ' + str(bdgt[2]))

    def on_budget_button_click(self):
        self.controller.update('Budget', {'monthly': float(self.edit_budget_monthly.text()),
                                          'weekly': float(self.edit_budget_weekly.text()),
                                          'daily': float(self.edit_budget_daily.text())})
        self.refresh_budgets()


    def refresh_categories(self):
        cats = self.controller.read('Category')
        self.category.addItems(cats)

    def on_create_category_button_click(self):
        # Обработка нажатия на кнопку "Создать категорию"
        pass

    def on_delete_category_button_click(self):
        # Обработка нажатия на кнопку "Удалить категорию"
        pass

    # Определение обработчика события
    def on_add_transaction_button_click(self):
        # Здесь можно добавить логику для открытия диалогового окна или других действий, связанных с добавлением транзакции
        pass





    # Декоратор для обертывания создания новой категории в транзакцию
    @db_session
    def on_create_category_button_click(self):
        new_category_name, ok_pressed = QInputDialog.getText(self, "Введите название категории", "Название категории:")

        if ok_pressed:
            new_category = Category(name=new_category_name)

    def on_add_transaction_button_click(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "New transaction":
            self.ui_window.btn_new_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.btn_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.dateEdit.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_window.le_description.text()
        balance = self.ui_window.le_balance.text()
        status = self.ui_window.cb_status.currentText()

        self.conn.add_new_transaction_query(date, category, description, balance, status)
        self.view_data()
        self.reload_data()
        self.new_window.close()




























