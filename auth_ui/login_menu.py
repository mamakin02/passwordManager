import sys

from PyQt6 import uic
from .login_widget import Ui_Login
from auth import AuthManager
from auth_ui.db_utils import get_db_connection, check_user_exists
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class LoginMenu(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        uic.loadUi('auth_ui/login.ui', self)
        self.setWindowTitle('Вход')
        self.setFixedSize(622, 312)

        self.btnLogin.clicked.connect(self.login)
        self.btnBack.clicked.connect(self.back_event)
        self.db = get_db_connection()
        self.show()

    def login(self):
        """функция для входа в аккаунт
        username - логин
        password - пароль"""
        username = self.lineLogin.text()
        password = self.linePassword.text()

        # проверка введенных данных
        if not username or not password:
            QMessageBox.critical(self, 'Ошибка', 'Пожалуйста, заполните все поля')
            return

        # проверка на существование пользователя
        if not check_user_exists(username):
            QMessageBox.critical(self, 'Ошибка', 'Пользователь не найден')
            return

        # выполнение входа
        if AuthManager.login(username, password):
            QMessageBox.information(self, 'Успешно', 'Вы успешно вошли в аккаунт')

            self.close()
            from selection_menu import SelectionMenu
            self.selection_menu = SelectionMenu()
            self.selection_menu.show()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Неправильное имя пользователя или пароль')
            return

    # кнопка назад
    def back_event(self):
        self.hide()
        from home_page import HomePage
        self.home_page = HomePage()
        self.home_page.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginMenu()
    ex.show()
    sys.exit(app.exec())