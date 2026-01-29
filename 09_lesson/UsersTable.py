from sqlalchemy import create_engine, text


class UsersTable:
    __scripts = {
        'insert users': text('INSERT INTO users (user_id, user_email, subject_id) '
                             'VALUES (:user_id, :user_email, :subject_id)'),
        'delete users': text('DELETE FROM users WHERE user_id = :user_id'),
        'select users': text('SELECT * FROM users'),
        'update users email': text('UPDATE users SET user_email = :user_email ')
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, user_id, user_email, subject_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['insert users'],
                               {'user_id': user_id, 'user_email': user_email,
                                'subject_id': subject_id})
        conn.commit()
        conn.close()

    def delete(self, user_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['delete users'],
                     {'user_id': user_id})
        conn.commit()
        conn.close()

    def get_users(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts['select users'])
        rows = result.mappings().all()
        conn.close()
        return rows

    def change_email(self, user_email):
        conn = self.__db.connect()
        conn.execute(self.__scripts['update users email'],
                     {'user_email': user_email})
        conn.commit()
        conn.close()
