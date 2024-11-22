import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from zxcvbn import zxcvbn

from ui_files.grade_widget import Ui_PasswordGrade


class GradePassword(QWidget, Ui_PasswordGrade):

    def __init__(self, id, username):
        super().__init__()
        uic.loadUi('ui_files/password_grade.ui', self)
        self.setWindowTitle('Оценка Пароля')

        self.setFixedSize(584, 472)

        # подключаем сигналы кнопки
        self.btnGrade.clicked.connect(self.password_grade)
        self.btnBack.clicked.connect(self.back_event)

        self.id = id
        self.username = username

    def password_grade(self):
        """ функция для оценки пароля

        password - пароль
        result - результат оценки пароля"""
        password = self.EditGrade.text()
        if not password:
            return

        result = zxcvbn(password)   # zxcvbn - библиотека для оценки пароля

        # смена цвета и текста в зависимости от оценки и количества баллов
        if result['score'] == 0:
            self.labelgrade.setStyleSheet('color: red')
            self.labelgrade.setText(f"Ваш пароль: {result['score'] * 10} баллов\n Плохой пароль")

        elif result['score'] == 1:
            self.labelgrade.setStyleSheet('color: orange')
            self.labelgrade.setText(f"Ваш пароль: {result['score'] * 10 + 20} баллов\n Слабый пароль")

        elif result['score'] == 2:
            self.labelgrade.setStyleSheet('color: yellow')
            self.labelgrade.setText(f"Ваш пароль: {result['score'] * 10 + 35} баллов\n Хороший пароль")

        elif result['score'] == 3:
            self.labelgrade.setStyleSheet('color: green')
            self.labelgrade.setText(f"Ваш пароль: {result['score'] * 10 + 45} баллов\n Отличный пароль")

        elif result['score'] == 4:
            self.labelgrade.setStyleSheet('color: blue')
            self.labelgrade.setText(f"Ваш пароль: {result['score'] * 10 + 60} баллов\n Превосходный пароль")

    # функция для перехода назад
    def back_event(self):
        from selection_menu import SelectionMenu
        self.hide()
        self.selection_menu = SelectionMenu(self.id, self.username)
        self.selection_menu.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GradePassword()
    ex.show()
    sys.exit(app.exec())
