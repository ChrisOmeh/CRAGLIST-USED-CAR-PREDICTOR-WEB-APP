from flask import Blueprint, render_template, url_for, redirect, request
from flask.helpers import flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    """
    This function is for signing up
    :return:
    """
    return render_template('signup.html')

@auth.route('/signup', methods = ['POST'])
def signup_post():
    """
    Main sign up function post code
    """
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #print(email, name, password)
    user = User.query.filter_by(email=email).first()
    print(user)

    if user:
        flash("Email already exist")
        return redirect(url_for('auth.signup'))
        
    new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))



@auth.route('/login')
def login():
    """
    This function is for LOGIN
    :return:
    """
    return render_template('login.html')

#LOGIN POST FUNCTION
@auth.route('/login', methods = ['POST'])
def login_post():
    """
    Main login post function
    """
    email = request.form.get('email')
    password = request.form.get('password')

    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))



@auth.route('/logout')
@login_required
def logout():
    """
    This function is for logging out
    :return:
    """
    logout_user()
    return redirect(url_for('main.index'))
