import json
from flask import request
from functools import wraps


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    if 'Authorization' not in request.headers:
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'Authorization header is expected.'
    }, 401)
    auth_header = request.headers.get('Authorization', None)

    headers_parts = auth_header.split(' ')

    if len(headers_parts) != 2:
        raise AuthError({
        'code': 'invalid_header',
        'description': 'Authorization header must be a bearer token.'
    }, 401)
    elif headers_parts[0].lower() != 'bearer':
        raise AuthError({
        'code': 'invalid_header',
        'description': 'Authorization header must start with "Bearer".'
    }, 401)

    return headers_parts[1]


def requires_auth_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = get_token_auth_header()
        return f(token, *args, **kwargs)
    return wrapper