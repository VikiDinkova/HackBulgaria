from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):
    def __init__(self, value=None):
        self.value = value

    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass


class TextField(BaseField):

    def __str__(self):
        return "<input type=\"text\">"


class EmailField(BaseField):
    def is_valid(self):
        return True

    def __str__(self):
        return "<input type=\"email\">"


class PasswordField(BaseField):
    def is_valid(self):
        return True

    def __str__(self):
        return "<input type=\"password\">"


class SubmitField(BaseField):
    def __str__(self):
        return "<input type=\"submit\">"


class Form(BaseField):
    def __init__(self, action, method):
        self.action = action
        self.method = method

    def __str__(self):
        return "<form action='{}', method='{}}'>".format(self.action, self.method)


class LoginForm(Form):
    name = TextField()
    password = PasswordField()
    submit = SubmitField()
