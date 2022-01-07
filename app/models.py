from app import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app



# Usuários 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
   

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
   
       
    def __repr__(self):
        return f'<User {self.name}>'


    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)




# Cadastro de veículos


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(64), unique=True)
    modelo = db.Column(db.String(64))
    fabricante = db.Column(db.String(64))
    renavan = db.Column(db.String(64), unique=True)
    combustivel = db.Column(db.String(64))
    lotacao = db.Column(db.String(64))
    anofabricacao = db.Column(db.String(64))
    manutencao = db.relationship('Maintenance', lazy=True)

    def __init__(self, placa, modelo, fabricante, renavan, combustivel, lotacao, anofabricacao):
        self.placa = placa
        self.modelo = modelo
        self.fabricante = fabricante
        self.renavan = renavan
        self.combustivel = combustivel
        self.lotacao = lotacao
        self.anofabricacao = anofabricacao

    def __repr__(self):
        return f'<Vehicle {self.placa}>'



# Cadastro de manutenção

class Maintenance(db.Model):
    __tablename__ = 'maintenance'
    id = db.Column(db.Integer, primary_key=True)
    orcamento_id = db.Column(db.String(64), unique=True)
    tipo_manutencao = db.Column(db.String(64))
    descricao = db.Column(db.String(128))
    quant_itens = db.Column(db.Integer)
    valor_unit = db.Column(db.Integer)
    valor_final = db.Column(db.Integer)
    hodometro = db.Column(db.Integer)    
    tabela_fipe = db.Column(db.String(64))
    veiculo = db.Column(db.Integer, db.ForeignKey('vehicles.placa'), nullable=False)

    def __init__(self, orcamento_id, tipo_manutencao, descricao, valor_unit, valor_final, tabela_fipe, quant_itens, hodometro):
        self.orcamento_id = orcamento_id
        self.tipo_manutencao = tipo_manutencao
        self.descricao = descricao
        self.quant_itens = quant_itens
        self.valor_unit = valor_unit
        self.valor_final = valor_final
        self.hodometro = hodometro
        self.tabela_fipe = tabela_fipe

    def __repr__(self):
        return f'Maintenance {self.orcamento_id}'