import bcrypt

from auth_ui.db_utils import get_db_connection, check_user_exists


class AuthManager:
    @staticmethod
    def register(username, password):
        """Зарегистрировать нового пользователя"""
        if check_user_exists(username):
            return False

        # хеширование пароля
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # сохранение в БД
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, master_password) VALUES (?, ?)",
                (username, hashed_password),
            )
            conn.commit()
        return True

    @staticmethod
    def login(username, password):
        """Выполнить вход пользователя"""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # получение пароля из БД
            cursor.execute(
                "SELECT master_password FROM users WHERE username = ?", (username,)
            )
            record = cursor.fetchone()

        # проверка пароля
        return record and bcrypt.checkpw(password.encode('utf-8'), record[0])
