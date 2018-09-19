from functools import wraps
from flask import session, url_for, redirect, request
from src.models.users.user_controller import User

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        return func(*args, **kwargs)
    return decorated_function

def requires_admin_permissions(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user_data = User.find_user_object_from_DB(session['email'])
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user', next=request.path))
        if user_data.user_role != "system_admin":
            return redirect(url_for('users.login_user'))
        return func(*args, **kwargs)
    return decorated_function