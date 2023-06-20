#Flask blueprint handling user authentication and lgin functionality

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__) #labelling this blueprint as 'auth' 

#Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #condition when 'submit' button is pressed
        username = request.form.get('username') #storing input username data
        password = request.form.get('password') #storing input password
        user = User.get(1)  # Get static user object with ID 1 from 'model.py' (username and password)

        if username == '' or password == '': #condition when either username or password is null or both
            flash("Null entry detected.", category='error') #pop up an error message
        elif not user or not user.check_password(password): #condition when either username or password or both do not match
            flash("Incorrect username or password, try again.", category='error') #pop up an error message
        else: #condition when both username and password matched
            flash("Logged in successfully!", category='success') #pop up a success message
            login_user(user, remember=True) #remember has logged in (only logged out automatically when page is restarted)
            return redirect(url_for('views.home')) #go to homepage

    return render_template("login.html", user=current_user) #when submit button on login page is not pressed, stay on login page

#Manual route
@auth.route('/manual') 
@login_required #this function is only accessible after successful login
def manual():
    return render_template("manual.html", user=current_user) #go to manual page

#Logout route
@auth.route('/logout')
@login_required #this function is only accessible after successful login
def logout():
    logout_user() #remember user has logged out
    flash("Logged out successfully!", category='success')
    return redirect(url_for('auth.login')) #go to login page




