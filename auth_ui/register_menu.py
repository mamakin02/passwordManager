import sys

from PyQt6 import uic
from auth import get_db_connection, check_user_exists
from .registration_widget import Ui_Registration
from auth import AuthManager
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class RegisrMenu(QWidget, Ui_Registration):
    def __init__(self):
        super().__init__()
        uic.loadUi('auth_ui/registration.ui', self)
        self.setWindowTitle('Регистрация')
        self.setFixedSize(622, 312)

        self.db = get_db_connection()
        self.btnReg.clicked.connect(self.register)
        self.btnBack.clicked.connect(self.back_event)
        self.show()

    def register(self):
        username = self.lineName.text()
        master_password = self.linePassword.text()

        if not username or not master_password:
            QMessageBox.critical(self, 'Ошибка', 'Пожалуйста, заполните все поля')
            return

        if check_user_exists(username):
            QMessageBox.critical(self, 'Ошибка', 'Пользователь с таким именем уже существует')
            return

        if AuthManager.register(username, master_password):
            QMessageBox.information(self, 'Успешно', 'Вы успешно зарегистрировались')

            self.close()
            from selection_menu import SelectionMenu
            self.selection_menu = SelectionMenu()
            self.selection_menu.show()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Неправильное имя пользователя или пароль')
            return

    def back_event(self):
        self.hide()
        from home_page import HomePage
        self.home_page = HomePage()
        self.home_page.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegisrMenu()
    ex.show()
    sys.exit(app.exec())
