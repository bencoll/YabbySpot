import functools
from typing import Callable

from flask import session, current_app, flash, redirect, url_for


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') is None:
            flash("You need to be logged in to access this resource.", 'warning')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function


def requires_writer(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') not in current_app.config.get('WRITER', 'EMPTY'):
            flash("You need to be a verified writer to create new posts.", 'danger')
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') not in current_app.config.get('ADMIN', 'EMPTY'):
            flash("You need to be an administrator to access this page.", 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
