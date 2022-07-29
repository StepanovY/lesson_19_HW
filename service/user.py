# Реализация бизнес-логики, за моделями обращаемся к DAO

import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        users = self.dao.get_all()
        return users

    def create(self, user_d):
        user_d['password'] = self.generate_password(user_d['password'])
        return self.dao.create(user_d)

    def update(self, user_d):
        user_d['password'] = self.generate_password(user_d['password'])
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_password(self, password):
        """
        Создание hash пароля
        :param password:
        :return:
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """
        Сравнение вводимого пароля и пароля, хранящегося в БД
        """
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256',
                                other_password.encode('utf-8'),
                                PWD_HASH_SALT,
                                PWD_HASH_ITERATIONS)
        )
