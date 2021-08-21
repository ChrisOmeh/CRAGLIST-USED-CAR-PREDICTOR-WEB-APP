from flask import Flask, Blueprint, render_template, url_for
from flask_login import login_required, current_user

main = Blueprint("main", __name__)


@main.route('/')
def index():
    """
    This function is for index page view/template
    :return:
    """
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    """
    This function is for the profile section
    :return:
    """
    return render_template('profile.html', name = current_user.name)


@main.route('/base')
def base():
    """
    This is the base.html file
    :return:
    """
    return render_template('base.html')
