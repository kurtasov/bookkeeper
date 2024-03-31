""" Модуль окна добавления трансакции пользовательского интерфейса программы"""
from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QTableWidget, QAbstractItemView)
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, QInputDialog)
from bookkeeper.controller.crud_controller import CrudController
from datetime import datetime
from bookkeeper.models.entities import *





from PySide6.QtWidgets import QHeaderView



from pony.orm import *
# Подключение к существующей базе данных

from bookkeeper.models.entities import Category
from bookkeeper.models.entities import Budget
from bookkeeper.models.entities import db


class AddWindow(QMainWindow):
    def __init__(self):
        super().__init__()



        self.controller = CrudController()
        self.setWindowTitle("Программа для ведения бюджета")
        self.setFixedSize(500, 500)

        self.layout = QVBoxLayout()

        self.date = QLabel('Дата: ')
        self.amount = QLabel('Сумма: ')
        self.comment = QLabel('Комментарий: ')
        self.layout.addWidget(self.date)
        self.edit_date = QLineEdit()
        self.layout.addWidget(self.edit_date)
        self.layout.addWidget(self.amount)
        self.edit_amount = QLineEdit()
        self.layout.addWidget(self.edit_amount)
        self.layout.addWidget(self.comment)
        self.edit_comment = QLineEdit()
        self.layout.addWidget(self.edit_comment)


        self.category = QComboBox(self)
        self.layout.addWidget(QLabel('Выберите категорию расхода:'))
        self.layout.addWidget(self.category)
        with db_session:
            categories = Category.select()
            for category in categories:
                self.category.addItem(category.name)





        self.budget_button = QPushButton('Записать расходы')
        self.layout.addWidget(self.budget_button)
        self.budget_button.clicked.connect(self.on_expense_button_click)




        # Определение обработчика события

        self.create_category_button = QPushButton('Создать категорию')
        self.layout.addWidget(self.create_category_button)
        self.create_category_button.clicked.connect(self.on_create_category_button_click)


        self.delete_category_button = QPushButton('Удалить категорию')
        self.layout.addWidget(self.delete_category_button)
        self.delete_category_button.clicked.connect(self.on_delete_category_button_click)


        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)



    def set_controller(self, controller):
        self.controller = controller

    def create_expense(self):
        params = {
            'amount': float(self.edit_amount.text()),
            'expense_date': datetime.strptime(self.edit_date.text(), '%d.%m.%y'),
            'comment': str(self.edit_comment.text()),
            'category_id': self.category.currentIndex()  # Пример значения идентификатора категории
        }

        expr = self.controller.create('Expense', params)
        self.amount.setText('Сумма: ' )
        self.date.setText('Дата: ')
        self.comment.setText('Комментарий: ')






    def on_expense_button_click(self):
        expense_date = datetime.strptime(self.edit_date.text(), '%d.%m.%y')
        self.controller.create('Expense', {
            'amount': float(self.edit_amount.text()),
            'expense_date': expense_date,
            'comment': str(self.edit_comment.text()),
            'category_id': self.category.currentIndex()  # Предполагая, что 'category' должен быть выбран из QComboBox
        })
        self.create_expense()







    def refresh_categories(self):
        cats = self.controller.read('Category')
        self.category.addItems(cats)

    def on_create_category_button_click(self):
        # Обработка нажатия на кнопку "Создать категорию"
        pass

    def on_delete_category_button_click(self):
        # Обработка нажатия на кнопку "Удалить категорию"
        pass






    # Декоратор для обертывания создания новой категории в транзакцию
    @db_session
    def on_create_category_button_click(self):
        new_category_name, ok_pressed = QInputDialog.getText(self, "Введите название категории", "Название категории:")

        if ok_pressed:
            new_category = Category(name=new_category_name)




