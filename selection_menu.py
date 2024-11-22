import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget

from generate_pass import GeneratePassword
from grade_my_pass import GradePassword
from home_page import HomePage
from table_passwords import DataBase
from ui_files.selection_widget import Ui_SelectionMenu


class SelectionMenu(QWidget, Ui_SelectionMenu):

    def __init__(self, id=None, username=None):
        super().__init__()
        uic.loadUi('ui_files/selection_menu.ui', self)
        self.setWindowTitle('Меню выбора')
        self.setFixedSize(527, 523)

        self.btnGotoGenerate.clicked.connect(self.goto_generate)
        self.btnGotoGrade.clicked.connect(self.goto_grade)

        self.id = id
        self.username = username

        if (self.id is not None) and (self.username is not None):
            self.btnMyPass.clicked.connect(self.goto_my_pass)
        else:
            self.btnMyPass.hide()
        self.btnBack.clicked.connect(self.back_event)

        # инициализируем классы
        self.generate_pass = None
        self.grade_pass = None
        self.home_page = None
        self.data_base = None
        self.home_page = None

    # функции перехода к генератору паролей
    def goto_generate(self):
        self.hide()
        if self.generate_pass is None:
            self.generate_pass = GeneratePassword(self.id, self.username)
        self.generate_pass.show()

    # функции перехода к оценке паролей
    def goto_grade(self):
        self.hide()
        if self.generate_pass is None:
            self.generate_pass = GradePassword(self.id, self.username)
            self.generate_pass.show()

    # функции перехода к таблице с паролямм
    def goto_my_pass(self):
        self.data_base = DataBase(self.id, self.username)
        self.hide()
        self.data_base.show()

    # функция перехода назад на страницу главного меню
    def back_event(self):
        self.hide()
        if self.home_page is None:
            self.home_page = HomePage()
            self.home_page.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SelectionMenu()
    ex.show()
    sys.exit(app.exec())
