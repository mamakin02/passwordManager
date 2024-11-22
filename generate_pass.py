import random
import string
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QInputDialog, QMessageBox, QWidget
from zxcvbn import zxcvbn

from table_passwords import DataBase
from ui_files.generate_widget import Ui_GenerationPassword


class GeneratePassword(QWidget, Ui_GenerationPassword):
    def __init__(self, id, username):
        super().__init__()
        uic.loadUi('ui_files/generation_password.ui', self)
        self.setWindowTitle('Генератор паролей')
        self.setFixedSize(647, 506)

        # устанавливаем максимум и минимум длины пароля
        self.lenghtSlider.setMaximum(30)
        self.lenghtSlider.setMinimum(4)

        # наборы символов
        self.symbols = '!@#$%^&*()_+}[]|:<>?{'
        self.lower_letters = string.ascii_letters.lower()
        self.upper_letters = self.lower_letters.upper()
        self.digits = string.digits

        # подключаем сигналы
        self.lenghtSlider.valueChanged.connect(self.select_lenght)
        self.btnGenerate.clicked.connect(self.generate_password)
        self.btnBack.clicked.connect(self.back_event)

        self.id = id
        self.username = username

        if (self.id is not None) and (self.username is not None):
            self.btnSave.clicked.connect(self.save_password)
        else:
            self.btnSave.hide()

        # по умолчанию выключены все чекбоксы
        self.checkUpper.setChecked(False)
        self.checkLower.setChecked(False)
        self.checkDigits.setChecked(False)
        self.checkSymbols.setChecked(False)

        self.db = DataBase(self.id, self.username)

    # функция для выбора длины пароля
    def select_lenght(self):
        value = self.lenghtSlider.value()
        self.passwordLine.setText(f"Выберите длину пароля: {value}")

    def generate_password(self):
        """
        Функция для генерации пароля

        value - длина пароля
        characters - набор символов
        password - пароль
        """
        value = self.lenghtSlider.value()

        characters = ''

        # выбираем категории пароля
        if self.checkUpper.isChecked():
            characters += self.upper_letters
        if self.checkLower.isChecked():
            characters += self.lower_letters
        if self.checkDigits.isChecked():
            characters += self.digits
        if self.checkSymbols.isChecked():
            characters += self.symbols

        # если ни одна категория не выбрана выдаем сообщение об ошибке
        if not characters:
            self.passwordLine.setText('Выберите хотя бы 1 категорию')
            return

        # генерируем пароль
        password = ''.join(random.choice(characters) for _ in range(value))
        self.passwordLine.setText(password)

        self.password_strength()

    def password_strength(self):
        """
        Функция для оценки сложности пароля

        password - пароль
        result - результат оценки пароля
        """
        password = self.passwordLine.text()
        if not password:
            return
        result = zxcvbn(password)   # zxcvbn - библиотека для оценки пароля

        # устанавливаем цвета в зависимости от сложности пароля
        if result['score'] == 0:
            self.passwordGrade.settext('Плохой пароль')
            self.passwordGrade.setStyleSheet('color: red')
        if result['score'] == 1:
            self.passwordGrade.setText('Слабый пароль')
            self.passwordGrade.setStyleSheet('color: orange')
        if result['score'] == 2:
            self.passwordGrade.setText('Хороший пароль')
            self.passwordGrade.setStyleSheet('color: yellow')
        if result['score'] == 3:
            self.passwordGrade.setText('Отличный пароль')
            self.passwordGrade.setStyleSheet('color: green')
        if result['score'] == 4:
            self.passwordGrade.setText('Превосходный пароль')
            self.passwordGrade.setStyleSheet('color: blue')

    # функция для возврата в меню
    def back_event(self):
        from selection_menu import SelectionMenu
        self.hide()
        self.selection_menu = SelectionMenu(self.id, self.username)
        self.selection_menu.show()

    def save_password(self):
        """
        Функция для сохранения пароля

        password - пароль
        username - логин
        user_id - id пользователя
        """
        password = self.passwordLine.text()
        if not password:
            return

        # сохраняем пароль
        self.db.add_password(password)
        QMessageBox.information(self, 'Успех', 'Пароль сохранен')

        self.hide()
        self.db.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GeneratePassword()
    ex.show()
    sys.exit(app.exec())
