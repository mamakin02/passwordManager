import sys

from PyQt6 import QtGui, uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget

from ui_files.home_widget import Ui_HomePage


class HomePage(QWidget, Ui_HomePage):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/home_page.ui', self)
        self.setWindowTitle('Главная Страница')

        # подключаем сигналы кнопки
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister.clicked.connect(self.register)
        self.btnWithoutReg.clicked.connect(self.enter_without_reg)
        self.setFixedSize(415, 518)

        # изменяем цвет текста в заголовке
        palette = self.name.palette()
        palette.setColor(QtGui.QPalette.ColorRole.WindowText, QtGui.QColor("#6eb999"))
        self.name.setPalette(palette)

        self.without_reg_flag = False

    # Функция для открытия окна входа
    def login(self):
        self.hide()
        from auth_ui.login_menu import LoginMenu
        self.login_window = LoginMenu()
        self.login_window.show()

    # Функция для открытия окна регистрации
    def register(self):
        self.hide()
        from auth_ui.register_menu import RegisrMenu
        self.register_window = RegisrMenu()
        self.register_window.show()

    def enter_without_reg(self):
        """
        Функция для входа без регистрации
        reply - ответ от пользователя
        """
        reply = QMessageBox.question(
            self,
            'Вход Без Регистрации',
            'Вы уверены, что хотите войти без регистрации?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # дейсвия если пользователь подтвердил вход без регистрации
            print("Пользователь выбрал вход без регистрации.")
            from selection_menu import SelectionMenu
            self.hide()
            self.selection_menu = SelectionMenu()
            self.selection_menu.show()
        else:
            # дейсивия если пользователь отказался
            print("Пользователь отменил вход без регистрации.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomePage()
    ex.show()
    sys.exit(app.exec())
