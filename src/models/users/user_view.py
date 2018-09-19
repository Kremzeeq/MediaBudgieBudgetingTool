
from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect

from src.models.central_budgets.central_budget_controller import Central_budget
from src.models.users.user_controller import User
import src.models.users.user_errors as UserErrors

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/auth', methods=['GET','POST'])
def authenticate_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.authenticate_user(email, password):
                return redirect(url_for("users.register_user"))
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/auth.html")

@user_blueprint.route('/register', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for("users.budget_portal"))
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/register.html")


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.validate_user_login(email, password):
                session['email'] = email
                return redirect(url_for("users.budget_portal"))
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/login.html")

@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('home'))

@user_blueprint.route('/portal')
def budget_portal():
    return render_template("users/portal.html")