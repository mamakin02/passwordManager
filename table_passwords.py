import sys

from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QHeaderView, QTableWidgetItem,
                             QWidget)

from ui_files.table_widget import Ui_DataBase


class DataBase(QWidget, Ui_DataBase):

    def __init__(self, id, username):
        super().__init__()
        uic.loadUi('ui_files/table_passwords.ui', self)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setFixedSize(721, 673)

        self.btnBack.clicked.connect(self.back_event)
        self.btnClear.clicked.connect(self.clear_table)

        self.id = id
        self.username = username

        self.load_data()

    # кнопка назад
    def back_event(self):
        self.close()
        from selection_menu import SelectionMenu
        self.selection_menu = SelectionMenu(self.id, self.username)
        self.selection_menu.show()

    def load_data(self):
        """Загрузка данных в таблицу"""
        from auth_ui.db_utils import get_db_connection

        # подключение к БД
        connection = get_db_connection()
        cursor = connection.cursor()

        # получение данных
        query = f"SELECT password FROM passwords WHERE user_id = {self.id}"

        cursor.execute(query)

        # запись данных в таблицу
        results = cursor.fetchall()
        self.table.setRowCount(len(results))
        self.table.setColumnCount(1)

        # заполнение таблицы
        for row_number, row_data in enumerate(results):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        cursor.close()
        connection.close()

    def add_password(self, password):
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
        cursor.execute(query, (self.id, self.username, password))
        connection.commit()

        cursor.close()
        connection.close()

        self.load_data()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataBase()
    ex.show()
    sys.exit(app.exec())
