from flask import Blueprint


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register')
def register_user():
    return 'users.register_user'


@user_blueprint.route('/login')
def login_user():
    return 'users.login_user'


@user_blueprint.route('/logout')
def logout_user():
    return 'users.logout_user'
