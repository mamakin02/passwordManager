import sqlite3


# подключение к БД
def get_db_connection():
    conn = sqlite3.connect('database/data_passwords.sqlite3')
    return conn


# проверка на существование пользователя
def check_user_exists(username):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return bool(cursor.fetchone())


def get_user_id(username):
    from auth_ui.db_utils import get_db_connection

    connection = get_db_connection()
    cursor = connection.cursor()

    # получение id
    query = "SELECT id FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    id = cursor.fetchone()[0]

    return id
