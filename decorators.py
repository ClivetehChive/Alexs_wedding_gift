from functools import wraps
from flask_login import current_user
from flask import abort
from .models import Role

def role_allowed(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(role):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def role_not_allowed(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(role):
                return f(*args, **kwargs)
            else:
                abort(403)
        return decorated_function
    return decorator

def admin_required(f):
    return role_allowed("Admin")(f)

def remote_not_allowed(f):
    return role_not_allowed("Remote")(f)