from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from common import CustomErrors
from common.decorators import requires_admin
from models.user import User

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        # User has submitted information for registration
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(first_name, last_name, email, password)
            session['email'] = email
            session['name'] = first_name
            flash("You are now logged in. Welcome!", 'success')
            return redirect(url_for('index'))
        except CustomErrors.CustomError as e:
            flash(e.message, 'danger')
    return render_template('user/register_form.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        # user attempting to log in
        email = request.form['email']
        password = request.form['password']

        try:
            User.attempt_login(email, password)
            session['email'] = email
            session['name'] = User.find_by_email(email).first_name
            return redirect(url_for('index'))
        except CustomErrors.CustomError as e:
            flash(e.message, 'error')
    return render_template('user/login_form.html')


@user_blueprint.route('/logout')
def logout_user():
    if session.get('email') is None:
        flash("You cannot do that as you are not logged in.", "error")
    session.pop('email', None)
    session.pop('name', None)
    return redirect(url_for('index'))


@user_blueprint.route('/recover')
@requires_admin
def recover_account():
    return 'users.recover_account GET'
