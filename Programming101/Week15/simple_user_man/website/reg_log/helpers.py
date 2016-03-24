from .models import User


def user_exists(email):
    try:
        User.objects.get(email=email)
        return True
    except User.DoesNotExist:
        return False

def login()
