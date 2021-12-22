from flask import render_template, redirect, request, url_for, flash
from flask_wtf import form
from  ..models import User
from wtforms.validators import Email, DataRequired
from app.auth import forms
from . import auth
from app import db
from .forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, login_required, current_user




@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    email=form.email.data
    name=form.name.data
    password=form.password.data
    
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email, name, password)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('auth.login')) 
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(password):
            login_user(user, form.remember_me.data)    
            return redirect(url_for('auth.profile'))

    else:
        return render_template('auth/login.html', form=form)


@auth.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))