import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QWidget, QHeaderView,
                             QTableWidgetItem)
from ui_files.table_widget import Ui_DataBase


class DataBase(QWidget, Ui_DataBase):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui_files/table_passwords.ui', self)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setFixedSize(721, 673)

        self.btnBack.clicked.connect(self.back_event)
        self.btnClear.clicked.connect(self.clear_table)

    # кнопка назад
    def back_event(self):
        self.close()
        from selection_menu import SelectionMenu
        self.selection_menu = SelectionMenu()
        self.selection_menu.show()

    def load_data(self):
        """Загрузка данных в таблицу"""
        from auth_ui.db_utils import get_db_connection
        # подключение к БД
        connection = get_db_connection()
        cursor = connection.cursor()

        # получение данных
        query = "SELECT username, password, user_id FROM passwords"
        cursor.execute(query)

        # запись данных в таблицу
        results = cursor.fetchall()
        self.table.setRowCount(len(results))
        self.table.setColumnCount(3)

        # заполнение таблицы
        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        cursor.close()
        connection.close()

    def add_password(self, username, password, user_id):
        """Добавление пароля в таблицу

        username - логин
        password - пароль
        user_id - id пользователя"""
        # подключение к БД
        from auth_ui.db_utils import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # добавление пароля
        query = "INSERT INTO passwords (user_id, username, password) VALUES (?, ?, ?)"
        cursor.execute(query, (user_id, username, password))
        connection.commit()

        cursor.close()
        connection.close()

        self.load_data()

    def get_user_id(self, username):
        from auth_ui.db_utils import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # получение id
        query = "SELECT id FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        # возврат id
        if result:
            return result[0]
        return None

    def add_user(self, username):
        from auth_ui.db_utils import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # добавление пользователя
        query = "INSERT INTO users (username) VALUES (?)"
        cursor.execute(query, (username,))
        connection.commit()

        # получение id
        user_id = cursor.lastrowid   # получение id последней записи
        cursor.close()
        connection.close()

        return user_id

    def clear_table(self):
        from auth_ui.db_utils import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # очистка таблицы
        query = "DELETE FROM passwords"
        cursor.execute(query)
        connection.commit()

        cursor.close()
        connection.close()

        self.load_data()

    def check_user(self):
        from home_page import HomePage
        home_page = HomePage()

        if home_page.without_reg_flag:
            return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataBase()
    ex.show()
    sys.exit(app.exec())
