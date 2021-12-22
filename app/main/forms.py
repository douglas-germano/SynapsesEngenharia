from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from app.models import Vehicle
from wtforms import ValidationError



class RegisterVehicleForm(FlaskForm):
    placa = StringField('Placa do Veículo:', validators=[DataRequired(), Length(1, 64)])
    anofabricacao = StringField('Ano de Fabricação:', validators=[DataRequired(), Length(1, 64)])
    modelo = StringField('Modelo do Veículo:', validators=[DataRequired(), Length(1, 64)])
    fabricante = StringField('Fabricante do Veículo:', validators=[DataRequired(), Length(1, 64)])
    renavan = StringField('Renavan:', validators=[DataRequired(), Length(1, 64)])
    combustivel = StringField('Combustível:', validators=[DataRequired(), Length(1, 64)])
    lotacao = StringField('Lotação do Veículo:', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Registrar Veículo')

    def validate_vehicle(self, field):
        if Vehicle.query.filter_by(vehicles=field.data.lower()).first():
            raise ValidationError('Veículo já Registrado.')