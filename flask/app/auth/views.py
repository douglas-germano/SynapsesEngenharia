from flask import render_template, redirect, request, url_for, flash
from flask_wtf import form
from  ..models import User
from wtforms.validators import Email, DataRequired
from app.auth import forms
from . import auth
from app import db
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required, current_user
from ..email import send_email





@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    cpf=form.cpf.data
    email=form.email.data
    name=form.name.data 
    password=form.password.data

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(cpf, email, name, password)
            db.session.add(user)
            db.session.commit()
            token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)                  
        flash('A confirmation email has been sent to you by email.')

        return redirect(url_for('auth.login'))

    else:
        return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('auth.profile'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('auth.login'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user, token=token)         
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))


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
