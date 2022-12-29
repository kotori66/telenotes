import sqlite3


class SqlCrud:
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute(
                'SELECT `user_id` FROM `users` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute('INSERT INTO users(user_id) VALUES(?)', (user_id,))

    def set_note(self, note, user_id):
        """Добавляем заметку в БД"""
        with self.connection:
            return self.cursor.execute(
                'INSERT INTO notes(note, user_key) VALUES(?, ?)', (note, user_id))

    def get_all_notes(self, user_id):
        """Возвращает все заметки с БД"""
        with self.connection:
            return self.cursor.execute(
                'SELECT id, note, date FROM notes WHERE user_key = ?', (user_id,)).fetchall()

    def get_note(self, user_id, note):
        """Возвращает одну заметку из БД"""
        with self.connection:
            return self.cursor.execute(
                'SELECT title, text_notes FROM notes WHERE note = ? AND user_key = ?', (note, user_id)).fetchall()

    def delete_note(self, user_id, id_note):
        """Удаляет заметку"""
        with self.connection:
            return self.cursor.execute(
                'DELETE FROM notes WHERE id = ? AND user_key = ?', (id_note, user_id))

    def delete_all_notes(self, user_id):
        """Удаляет все заметки"""
        with self.connection:
            return self.cursor.execute(
                'DELETE FROM notes WHERE user_key = ?', (user_id,))
