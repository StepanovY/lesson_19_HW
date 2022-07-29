from dao.model.user import User


class UserDAO:
    """
    Класс с методами доступа к данным
    """

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Метод получения одного пользователя User
        """
        return self.session.query(User).get(uid)

    def get_by_username(self, username):
        """
        Метод поиска пользователя User по его имени (name)
        """
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        """
        Метод получения всех пользователей Users
        :return:
        """
        return self.session.query(User).all()

    def create(self, user_d):
        """
        Метод создания пользователя User
        :param user_d:
        :return:
        """
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        """
        Метод создания удаления User
        """
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        """
        Метод обновления данных о пользователе User
        """
        user = self.get_one(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
