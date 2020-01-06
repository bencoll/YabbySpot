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
    if session.get('email') is None:
        flash("You cannot do that as you are not logged in.", "warning")
    session.pop('email', None)
    return redirect(url_for('index'))


@user_blueprint.route('/recover')
def recover_account():
    return 'users.recover_account GET'
