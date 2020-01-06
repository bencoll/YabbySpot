from flask import Blueprint, request, render_template, session, redirect, url_for, flash

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # User has submitted information for registration
        return 'users.register_user POST'
    return render_template('user/register_form.html')


@user_blueprint.route('/login')
def login_user():
    return render_template('user/login_form.html')


@user_blueprint.route('/logout')
def logout_user():
    return 'users.logout_user'
