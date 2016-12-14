from functools import wraps
from flask import request, session, redirect
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

def _parse_token(auth):
    if auth is None:
        return 'No authorization header was found. The request has to be authenticated to access secured resources.', 401
    split = auth.split()
    if len(split) != 2:
        return 'Authorization header was not formatted correctly.', 400
    if split[0].lower() != 'bearer':
        return 'Only Bearer tokens are supported in the authentication header.', 400

def _get_token(auth):
    return auth.split()[1]

def secure(handle_unauthorized=True, cookie_authorization=False):
    def secure_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if cookie_authorization:
                if not ('user_id' in session):
                    return redirect('/auth/login')
                else:
                    result = func(*args, **kwargs)
                    return result

            authorization = request.headers.get('Authorization', None)
            err = _parse_token(authorization)
            if err != None: return err

            token_string = _get_token(authorization)

            token = None
            try:
                token = jwt.decode(token_string, SECRET, verify=VERIFY, algorithms=ALGORITHM, options=CHECKS, leeway=LEEWAY)
            except ExpiredSignatureError:
                return 'The authentication token has expired.', 401
            except:
                return 'Something went wrong when parsing the authentication header.', 400

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