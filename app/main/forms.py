from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from app.models import Maintenance, Vehicle
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


class EditVehicleForm(FlaskForm):
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


class MaintenanceForm(FlaskForm):
    orcamento = StringField('Número do orçamento:', validators=[DataRequired(), Length(1, 64)])
    tipo_manutencao = StringField('Tipo de manutencao:', validators=[DataRequired(), Length(1, 64)])
    descricao = StringField('Descrição:', validators=[DataRequired(), Length(1, 64)])
    quant_itens = StringField('Quantidade de Itens:', validators=[DataRequired(), Length(1, 64)])
    valor_unitario = StringField('Valor unitário:', validators=[DataRequired(), Length(1, 64)])
    valor_final = StringField('Valor final:', validators=[DataRequired(), Length(1, 64)])
    hodometro = StringField('Hodometro/Horimetro:', validators=[DataRequired(), Length(1, 64)])
    tabela_fipe = StringField('Tabela FIPE ayial:', validators=[DataRequired(), Length(1, 64)])
    placa = StringField('Placa do Veículo:', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Registrar Manutenção')

    def validate_vehicle(self, field):
        if Maintenance.query.filter_by(vehicles=field.data.lower()).first():
            raise ValidationError('Manutenção já Registrada.')
