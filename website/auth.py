from flask import Blueprint, render_template
from flask_login import login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html' , user=current_user)

@auth.route('/logout')
def logout():
    return '<p>logout<p>'

@auth.route('/signup')
def signup():
    return render_template("signup.html", user=None)