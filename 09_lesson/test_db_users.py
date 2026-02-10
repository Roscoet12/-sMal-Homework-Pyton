from UsersTable import UsersTable
import os
from dotenv import load_dotenv
load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
mydatabase = os.getenv("MYDATABASE")

db = UsersTable(f'postgresql://{login}:{password}@localhost:5432/{mydatabase}')


def test_add_user():
    users = db.get_users()
    list_before = len(users)

    user_id = 98765
    user_email = "ksesh@email.com"
    subject_id = 1
    db.create(user_id, user_email, subject_id)

    users = db.get_users()
    list_after = len(users)

    db.delete(user_id)

    assert list_after - list_before == 1


def test_change_user_email():
    user_id = 98765
    user_email = "ksesh@email.com"
    subject_id = 1
    db.create(user_id, user_email, subject_id)

    new_email = "another_email@email.com"
    db.change_email(new_email, user_id)

    users = db.get_users()
    change_user = None
    for user in users:
        if user['user_email'] == new_email:
            change_user = user
            break

    db.delete(user_id)

    assert change_user is not None


def test_delete_users():
    user_id = 98765
    user_email = "ksesh@email.com"
    subject_id = 1
    db.create(user_id, user_email, subject_id)

    db.delete(user_id)

    users = db.get_users()
    delete_user = None
    for user in users:
        if user['user_id'] == user_id:
            delete_user = user
            break

    assert delete_user is None
