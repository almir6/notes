from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html' , user=current_user)

@auth.route('/logout')
def logout():
    return '<p>logout<p>'

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<6:
            flash('Email must be greater than 6 characters',category='error')
        elif len(firstname)<2:
            flash('Please input your first name', category='error')
        elif len(password1)<7:
            flash('Password needs to be at least 8 characters', category='error')
        elif password1 != password2:
            flash('Your passwords dont match', category='error')

        else:
            flash("Account created succesfully! ",category='success')


    return render_template("signup.html", user=None)