from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Length(1, 64), Email()])
    name = StringField('Nome Completo:', validators=[DataRequired(), Length(1, 64)])                   
    password = PasswordField('Sua senha:', validators=[DataRequired(), EqualTo('password2', message='As senhas devem ser iguais.')])
    password2 = PasswordField('Confirme sua senha:', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email Inválido.')
    

class LoginForm(FlaskForm):
    email = StringField('Digite seu Email:', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Digite sua senha:', validators=[DataRequired()])
    remember_me = BooleanField('Mantenha-me Logado')
    submit = SubmitField('Entrar.')
