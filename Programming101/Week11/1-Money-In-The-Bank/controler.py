from models import *
from helpers import hash_password
from datetime import datetime


class ClientAlreadyRegistered(Exception):
    pass


class UserNotExist(Exception):
    pass


class MainController:
    def register(self, username, password):
        user = self.session.query(Client).\
            filter(Client.username == username).first()

        if user is not None:
            raise ClientAlreadyRegistered('Client already registered')

        client = Client(username=username, password=password)
        self.__commit_object(client)

    def login(self, username, password):
        user = self.session.query(Client).\
            filter(Client.username == username).first()

        if user is None:
            return False

        pwd_hash, _ = hash_password(password, salt=user.salt)

        user = self.session.query(Client).\
            filter(Client.username=username, Client.password=pwd_hash).first()

        if user:
            return user
        else:
            return False

    def change_message(self, new_message, logged_user):
        user = self.session.query(Client).\
            filter(Client.id == logged_user.id).first()
        user.message = new_message
        self.__commit()

    def change_pass(self, new_pass, logged_user):
        user = self.session.query(Client).\
            filter(Client.id == logged_user.id).first()
        pwd_hash, salt = hash_password(new_pass)
        user.password, user.salt = pwd_hash, salt
        self.__commit()

    def create_login_attempt(self, username, status):
        user = self.session.query(Client).\
            filter(Client.username == username).first()
        if user is None:
            raise UserNotExist('Invalid username')
        log_attempt = LoginAttempt(attemps_status=status, client=user, timestamp=datetime.now())
        self.__commit_object(log_attempt)

    def __commit(self):
        self.session.commit()

    def __commit_object(self, obj):
        self.session.add(obj)
        self.__commit()

    def __commit_objects(self, objects):
        self.session.add_all(objects)
        self.__commit()

    def __init__(self, session):
        self.session = session
