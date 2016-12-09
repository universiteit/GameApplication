from functools import wraps
from flask import request
from threading import local

import jwt
from jwt import ExpiredSignatureError


SECRET = 'secret'
ALGORITHM = 'HS256'
VERIFY = True
LEEWAY = 0
CHECKS = {
    'verify_signature' : True,
    'verify_aud' : True, 
    'verify_iat' : True,
    'verify_exp' : True,
    'verify_nbf' : True,
    'verify_iss' : True,
    'verify_sub' : True,
    'verify_jti' : True,
    'leeway' : 0,
}

_context = None
def context():
    return _context


def secure(handle_unauthorized=True):
    def secure_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            authorization = request.headers.get('Authorization')

            if authorization is None:
                return 'No authorization header set. The request has to be authenticated to access secured resources.', 401
            
            token = None
            try:
                token = jwt.decode(authorization, SECRET, verify=VERIFY, algorithms=ALGORITHM, options=CHECKS, leeway=LEEWAY)
            except ExpiredSignatureError:
                return 'The authentication token has expired.', 401

            global _context
            _context = TokenContext(token)

            result = func(*args, **kwargs)

            _context = None

            return result
        return wrapper
    return secure_decorator


class Context(local):
    def __init__(self, user_id):
        self.user_id = user_id

class TokenContext(Context):
    def __init__(self, claims):
        super().__init__(claims['sub'])