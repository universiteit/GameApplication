from functools import wraps
from flask import request
from threading import local

from random import randint

context = None

def secure(handle_unauthorized=True):
    def secure_decorator(func):
        print('in secure')
        @wraps(func)
        def wrapper(*args, **kwargs):
            print ('in wrapper')
            authorization = request.headers.get('Authorization')

            global context
            if authorization is None:
                if handle_unauthorized:
                    return 'User is not logged in', 401
                context = Context(randint(0,100), None)
            else:
                context = Context(randint(0,100), authorization)


            result = func(*args, **kwargs)

            context = None

            return func(*args, **kwargs)
        return wrapper
    return secure_decorator


class Context(local):
    def __init__(user, auth):
        self.user = user
        self.authorization = auth
        self.authorized = True if auth != None else False